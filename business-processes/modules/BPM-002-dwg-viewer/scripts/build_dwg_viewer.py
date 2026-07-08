from __future__ import annotations

import argparse
import base64
import html
import json
import subprocess
from pathlib import Path

import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext, layout
from ezdxf.addons.drawing.svg import SVGBackend

ODA_EXE = Path(r"C:\Program Files\ODA\ODAFileConverter 27.1.0\ODAFileConverter.exe")


def run_oda(input_dir: Path, dxf_dir: Path, recursive: bool) -> None:
    dxf_dir.mkdir(parents=True, exist_ok=True)
    before = {p.resolve() for p in dxf_dir.rglob("*.dxf")}
    cmd = [
        str(ODA_EXE),
        str(input_dir),
        str(dxf_dir),
        "ACAD2018",
        "DXF",
        "1" if recursive else "0",
        "1",
        "*.DWG",
    ]
    subprocess.run(cmd, check=False)
    after = {p.resolve() for p in dxf_dir.rglob("*.dxf")}
    if not after - before and not after:
        raise RuntimeError(f"ODA did not create DXF files in {dxf_dir}")


def choose_layout(doc: ezdxf.EzDxf) -> object:
    return next((item for item in doc.layouts if item.name.lower() != "model"), doc.modelspace())


def render_svg(dxf_path: Path, svg_path: Path) -> None:
    doc = ezdxf.readfile(dxf_path)
    context = RenderContext(doc)
    backend = SVGBackend()
    Frontend(context, backend).draw_layout(choose_layout(doc), finalize=True)
    page = layout.Page(420, 297, units=layout.Units.mm)
    svg_path.write_text(backend.get_string(page), encoding="utf-8")


def data_uri_svg(svg_path: Path) -> str:
    raw = svg_path.read_bytes()
    return "data:image/svg+xml;base64," + base64.b64encode(raw).decode("ascii")


def find_matching_dxf(input_dir: Path, dxf_dir: Path, dwg_path: Path) -> Path | None:
    relative_dxf = dwg_path.relative_to(input_dir).with_suffix(".dxf")
    direct = dxf_dir / relative_dxf
    if direct.exists():
        return direct
    matches = sorted(dxf_dir.rglob(dwg_path.with_suffix(".dxf").name))
    return matches[0] if matches else None


def build_registry(input_dir: Path, dxf_dir: Path, preview_dir: Path) -> list[dict[str, object]]:
    preview_dir.mkdir(parents=True, exist_ok=True)
    registry: list[dict[str, object]] = []
    dwg_files = sorted([p for p in input_dir.rglob("*") if p.is_file() and p.suffix.lower() == ".dwg"])
    for index, dwg_path in enumerate(dwg_files, start=1):
        relative_path = dwg_path.relative_to(input_dir).as_posix()
        dxf_path = find_matching_dxf(input_dir, dxf_dir, dwg_path)
        svg_path = preview_dir / f"{index:04d}.svg"
        status = "ok"
        error = ""
        if dxf_path is None:
            status = "missing_dxf"
        else:
            try:
                render_svg(dxf_path, svg_path)
            except Exception as exc:  # keep batch processing alive
                status = "render_failed"
                error = str(exc)
        registry.append({
            "id": f"dwg-{index:04d}",
            "file_name": dwg_path.name,
            "relative_path": relative_path,
            "size_bytes": dwg_path.stat().st_size,
            "dxf_path": str(dxf_path) if dxf_path else "",
            "preview_file": svg_path.name if svg_path.exists() else "",
            "preview_data_uri": data_uri_svg(svg_path) if svg_path.exists() else "",
            "status": status,
            "error": error,
        })
    return registry


def render_html(registry: list[dict[str, object]], title: str) -> str:
    data_json = json.dumps(registry, ensure_ascii=False)
    title_html = html.escape(title)
    template = r'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__TITLE__</title>
  <style>
    :root { --bg:#fbfbfa; --panel:#f3f4f4; --nested:#e9ebeb; --border:#d5d8d8; --text:#1f2328; --muted:#59636e; --accent:#0969da; --shadow:0 1px 2px rgba(31,35,40,.08); font-family:"Segoe UI",-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif; }
    * { box-sizing:border-box; }
    html, body { width:100%; height:100%; }
    body { margin:0; height:100vh; height:100dvh; overflow:hidden; background:var(--bg); color:var(--text); overscroll-behavior:none; }
    .module-head { min-height:52px; padding:10px 12px; border-bottom:1px solid var(--border); background:#fff; display:grid; gap:4px; }
    h1 { margin:0; font-size:12px; line-height:1.25; font-weight:650; overflow-wrap:anywhere; }
    button { font:inherit; }
    .stats { color:var(--muted); font-size:12px; white-space:nowrap; }
    .app { height:100vh; display:grid; grid-template-columns:280px minmax(0,1fr); min-height:0; }
    .left { height:100%; min-height:0; border-right:1px solid var(--border); background:var(--panel); display:flex; flex-direction:column; min-width:0; }
    .search { display:none; padding:12px; border-bottom:1px solid var(--border); }
    input { width:100%; height:38px; border:1px solid var(--border); border-radius:6px; padding:0 10px; font:inherit; outline:none; background:#fff; }
    input:focus { border-color:var(--accent); box-shadow:0 0 0 3px rgba(9,105,218,.12); }
    .list { flex:1 1 auto; min-height:0; overflow-y:scroll; overflow-x:hidden; padding:10px; display:grid; gap:10px; align-content:start; scrollbar-gutter:stable; }
    .item { border:1px solid var(--border); border-radius:8px; background:#fff; padding:8px; cursor:pointer; box-shadow:var(--shadow); display:grid; gap:7px; text-align:left; }
    .item.active { outline:2px solid var(--accent); outline-offset:0; }
    .thumb { width:100%; aspect-ratio:4/3; object-fit:contain; background:var(--nested); border:1px solid var(--border); border-radius:6px; }
    .name { font-size:12px; font-weight:650; line-height:1.25; overflow-wrap:anywhere; }
    .path { font-size:11px; color:var(--muted); line-height:1.25; overflow-wrap:anywhere; }
    .right { min-width:0; min-height:0; display:grid; grid-template-rows:auto minmax(0,1fr); background:#fff; }
    .preview-head { min-height:52px; padding:8px 14px; border-bottom:1px solid var(--border); display:grid; grid-template-columns:minmax(0,1fr) auto; gap:10px; align-items:center; }
    .preview-title { font-size:13px; font-weight:650; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
    .preview-path { color:var(--muted); font-size:11px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
    .tools { display:flex; align-items:center; gap:6px; white-space:nowrap; }
    .tool { min-width:34px; height:32px; border:1px solid var(--border); border-radius:6px; background:#fff; color:var(--text); cursor:pointer; }
    .tool:hover { border-color:var(--accent); }
    .fit { padding:0 10px; }
    .zoom-label { min-width:48px; text-align:center; color:var(--muted); font-size:12px; }
    .preview { min-height:0; position:relative; background:var(--nested); overflow:auto; padding:0; cursor:grab; user-select:none; -webkit-user-select:none; touch-action:none; overscroll-behavior:contain; scrollbar-gutter:stable both-edges; }
    .preview.dragging { cursor:grabbing; }
    .canvas { box-sizing:content-box; position:relative; min-width:100%; min-height:100%; width:0; height:0; padding:64px; }
    .svg-wrap { display:block; width:max-content; height:max-content; background:#fff; border:1px solid var(--border); box-shadow:var(--shadow); }
    .svg-wrap svg { display:block; max-width:none; max-height:none; background:#fff; }
    .empty { color:var(--muted); text-align:center; padding:24px; margin:auto; }
    @media (max-width:760px) { body { height:100dvh; overflow:hidden; } .app { height:100dvh; min-height:0; grid-template-columns:1fr; grid-template-rows:38dvh minmax(0,62dvh); } .left { min-height:0; border-right:0; border-bottom:1px solid var(--border); } .module-head { min-height:40px; padding:7px 10px; } h1 { font-size:11px; } .stats { font-size:11px; } .list { grid-template-columns:repeat(2,minmax(0,1fr)); } .preview-head { min-height:40px; padding:6px 10px; grid-template-columns:minmax(0,1fr) auto; } .preview-title { font-size:11px; } .preview-path { display:none; } .tool { min-width:30px; height:28px; } .fit { padding:0 8px; } .zoom-label { min-width:42px; } }
    @media (orientation:landscape) and (max-height:520px) { .app { height:100dvh; grid-template-columns:230px minmax(0,1fr); grid-template-rows:1fr; } .module-head, .preview-head { min-height:38px; padding:5px 8px; } h1, .preview-title { font-size:11px; } .preview-path { display:none; } .tool { min-width:28px; height:26px; } .fit { padding:0 7px; } .zoom-label { min-width:40px; font-size:11px; } .list { padding:7px; gap:7px; } .item { padding:6px; gap:5px; } .name { font-size:11px; } .path { font-size:10px; } }
  </style>
</head>
<body>
  <main class="app">
    <aside class="left"><div class="module-head"><h1>__TITLE__</h1><div class="stats" id="stats"></div></div><div class="search"><input id="search" type="search" placeholder="Поиск по имени или пути"></div><div class="list" id="list"></div></aside>
    <section class="right">
      <div class="preview-head">
        <div><div class="preview-title" id="title">Выберите DWG</div><div class="preview-path" id="path"></div></div>
        <div class="tools" aria-label="Масштаб чертежа">
          <button class="tool" id="zoomOut" type="button" title="Уменьшить">-</button>
          <div class="zoom-label" id="zoomLabel">100%</div>
          <button class="tool" id="zoomIn" type="button" title="Увеличить">+</button>
          <button class="tool fit" id="zoomFit" type="button" title="Вписать в область">Вписать</button>
        </div>
      </div>
      <div class="preview" id="preview"><div class="empty">Слева выберите миниатюру чертежа.</div></div>
    </section>
  </main>
  <script>
    const files = __DATA_JSON__;
    const list = document.querySelector('#list');
    const search = document.querySelector('#search');
    const stats = document.querySelector('#stats');
    const titleEl = document.querySelector('#title');
    const pathEl = document.querySelector('#path');
    const preview = document.querySelector('#preview');
    const zoomOut = document.querySelector('#zoomOut');
    const zoomIn = document.querySelector('#zoomIn');
    const zoomFit = document.querySelector('#zoomFit');
    const zoomLabel = document.querySelector('#zoomLabel');
    let activeId = null;
    let currentSvg = null;
    let currentWrap = null;
    let currentCanvas = null;
    let currentBox = { w: 420, h: 297 };
    let fitScale = 1;
    let zoom = 1;
    let dragging = false;
    let lastPoint = { x: 0, y: 0 };

    function norm(v) { return String(v || '').toLowerCase().replaceAll('ё','е'); }
    function clamp(v, min, max) { return Math.max(min, Math.min(max, v)); }
    function svgMarkup(dataUri) {
      if (!dataUri) return '';
      const b64 = dataUri.split(',')[1] || '';
      const bytes = Uint8Array.from(atob(b64), c => c.charCodeAt(0));
      return new TextDecoder('utf-8').decode(bytes);
    }
    function readSvgBox(svg) {
      const vb = svg.viewBox && svg.viewBox.baseVal;
      if (vb && vb.width && vb.height) return { w: vb.width, h: vb.height };
      const w = parseFloat(svg.getAttribute('width')) || 420;
      const h = parseFloat(svg.getAttribute('height')) || 297;
      return { w, h };
    }
    function applyZoom(anchor, oldZoom = zoom) {
      if (!currentSvg || !currentWrap || !currentCanvas) return;
      const ratio = oldZoom ? zoom / oldZoom : 1;
      const point = anchor || { x: preview.clientWidth / 2, y: preview.clientHeight / 2 };
      const w = Math.ceil(currentBox.w * fitScale * zoom);
      const h = Math.ceil(currentBox.h * fitScale * zoom);
      const padX = Math.max(72, Math.round(preview.clientWidth * 0.5));
      const padY = Math.max(72, Math.round(preview.clientHeight * 0.5));
      currentSvg.style.width = `${w}px`;
      currentSvg.style.height = `${h}px`;
      currentWrap.style.width = `${w}px`;
      currentWrap.style.height = `${h}px`;
      currentCanvas.style.width = `${w}px`;
      currentCanvas.style.height = `${h}px`;
      currentCanvas.style.padding = `${padY}px ${padX}px`;
      zoomLabel.textContent = `${Math.round(zoom * 100)}%`;
      if (anchor) {
        preview.scrollLeft = (preview.scrollLeft + point.x) * ratio - point.x;
        preview.scrollTop = (preview.scrollTop + point.y) * ratio - point.y;
      }
    }
    function fitCurrent() {
      if (!currentSvg) return;
      currentBox = readSvgBox(currentSvg);
      const availableW = Math.max(120, preview.clientWidth - 52);
      const availableH = Math.max(120, preview.clientHeight - 52);
      fitScale = Math.min(availableW / currentBox.w, availableH / currentBox.h);
      zoom = 1;
      applyZoom();
      preview.scrollLeft = 0;
      preview.scrollTop = 0;
    }
    function setZoom(next, anchor) {
      const oldZoom = zoom;
      zoom = clamp(next, 0.25, 12);
      applyZoom(anchor, oldZoom);
    }
    function show(file, rerender = true) {
      activeId = file.id;
      titleEl.textContent = file.file_name;
      pathEl.textContent = file.relative_path;
      currentSvg = null;
      currentWrap = null;
      currentCanvas = null;
      if (file.preview_data_uri) {
        preview.innerHTML = `<div class="canvas"><div class="svg-wrap">${svgMarkup(file.preview_data_uri)}</div></div>`;
        currentSvg = preview.querySelector('svg');
        currentWrap = preview.querySelector('.svg-wrap');
        currentCanvas = preview.querySelector('.canvas');
        if (currentSvg) fitCurrent();
      } else {
        preview.innerHTML = `<div class="empty">Превью не создано: ${file.status}</div>`;
        zoomLabel.textContent = '100%';
      }
      if (rerender) render();
    }
    function render() {
      const q = norm(search.value);
      const shown = files.filter(f => !q || norm(f.file_name + ' ' + f.relative_path).includes(q));
      stats.textContent = `DWG: ${shown.length} из ${files.length}`;
      list.innerHTML = '';
      for (const file of shown) {
        const el = document.createElement('button');
        el.className = 'item' + (file.id === activeId ? ' active' : '');
        el.type = 'button';
        el.innerHTML = `${file.preview_data_uri ? `<img class="thumb" src="${file.preview_data_uri}" alt="">` : `<div class="thumb"></div>`}<div class="name"></div><div class="path"></div>`;
        el.querySelector('.name').textContent = file.file_name;
        el.querySelector('.path').textContent = file.relative_path;
        el.addEventListener('mouseenter', () => show(file, false));
        el.addEventListener('focus', () => show(file, false));
        el.addEventListener('click', () => show(file, true));
        list.appendChild(el);
      }
    }

    zoomOut.addEventListener('click', () => setZoom(zoom / 1.25));
    zoomIn.addEventListener('click', () => setZoom(zoom * 1.25));
    zoomFit.addEventListener('click', fitCurrent);
    preview.addEventListener('wheel', event => {
      if (!currentSvg || !event.ctrlKey) return;
      event.preventDefault();
      const rect = preview.getBoundingClientRect();
      const anchor = { x: event.clientX - rect.left, y: event.clientY - rect.top };
      setZoom(zoom * (event.deltaY < 0 ? 1.15 : 1 / 1.15), anchor);
    }, { passive:false });
    preview.addEventListener('pointerdown', event => {
      if (!currentSvg || event.button !== 0) return;
      dragging = true;
      lastPoint = { x: event.clientX, y: event.clientY };
      preview.classList.add('dragging');
      preview.setPointerCapture(event.pointerId);
    });
    preview.addEventListener('pointermove', event => {
      if (!dragging) return;
      event.preventDefault();
      preview.scrollLeft -= event.clientX - lastPoint.x;
      preview.scrollTop -= event.clientY - lastPoint.y;
      lastPoint = { x: event.clientX, y: event.clientY };
    });
    function stopDrag(event) {
      dragging = false;
      preview.classList.remove('dragging');
      if (event && preview.hasPointerCapture(event.pointerId)) preview.releasePointerCapture(event.pointerId);
    }
    preview.addEventListener('pointerup', stopDrag);
    preview.addEventListener('pointercancel', stopDrag);
    preview.addEventListener('touchstart', event => {
      if (!currentSvg || !event.touches.length) return;
      event.preventDefault();
      dragging = true;
      lastPoint = { x: event.touches[0].clientX, y: event.touches[0].clientY };
      preview.classList.add('dragging');
    }, { passive:false });
    preview.addEventListener('touchmove', event => {
      if (!dragging || !event.touches.length) return;
      event.preventDefault();
      const touch = event.touches[0];
      preview.scrollLeft -= touch.clientX - lastPoint.x;
      preview.scrollTop -= touch.clientY - lastPoint.y;
      lastPoint = { x: touch.clientX, y: touch.clientY };
    }, { passive:false });
    preview.addEventListener('touchend', event => stopDrag(event));
    preview.addEventListener('touchcancel', event => stopDrag(event));    window.addEventListener('resize', fitCurrent);
    search.addEventListener('input', render);
    render();
    if (files.length) show(files[0], true);
  </script>
</body>
</html>'''
    return template.replace("__TITLE__", title_html).replace("__DATA_JSON__", data_json)

def main() -> None:
    parser = argparse.ArgumentParser(description="Build a standalone DWG HTML viewer from a local DWG folder.")
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--title", default="DWG Viewer")
    parser.add_argument("--recursive", action="store_true", default=True)
    args = parser.parse_args()

    if not ODA_EXE.exists():
        raise RuntimeError(f"ODA File Converter not found: {ODA_EXE}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    dxf_dir = args.output_dir / "dxf"
    preview_dir = args.output_dir / "previews"
    run_oda(args.input_dir, dxf_dir, args.recursive)
    registry = build_registry(args.input_dir, dxf_dir, preview_dir)
    (args.output_dir / "registry.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output_dir / "index.html").write_text(render_html(registry, args.title), encoding="utf-8")
    print(f"DWG files: {len(registry)}")
    print(f"HTML: {args.output_dir / 'index.html'}")


if __name__ == "__main__":
    main()
