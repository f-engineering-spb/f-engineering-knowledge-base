import os
import re
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

REWRITES = {}
HTACCESS_PATH = os.path.join(CURRENT_DIR, "htaccess")
if not os.path.exists(HTACCESS_PATH):
    HTACCESS_PATH = os.path.join(CURRENT_DIR, ".htaccess")

if os.path.exists(HTACCESS_PATH):
    with open(HTACCESS_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"^RewriteRule\s+\^([^$\/]+)\$?\s+([^\s]+)", line, re.IGNORECASE)
            if m:
                src = m.group(1).strip("^$")
                dst = m.group(2)
                REWRITES[src.lower()] = dst
                REWRITES["/" + src.lower()] = dst

class CleanURLHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=CURRENT_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        clean_path = parsed.path.strip("/").lower()

        if clean_path in REWRITES:
            target_file = REWRITES[clean_path]
            self.path = "/" + target_file
        elif clean_path == "" or clean_path == "index":
            self.path = "/index.html"
        elif clean_path == "brandbook":
            self.path = "/brandbook.html"

        return super().do_GET()

    def end_headers(self):
        if self.path.endswith(".html") or self.path.endswith("archive"):
            self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

if __name__ == "__main__":
    import webbrowser
    import threading

    PORT = 8080
    server_address = ("", PORT)
    try:
        httpd = ThreadingHTTPServer(server_address, CleanURLHandler)
    except OSError:
        PORT = 8088
        server_address = ("", PORT)
        httpd = ThreadingHTTPServer(server_address, CleanURLHandler)

    url = f"http://localhost:{PORT}/"
    print(f"===================================================")
    print(f"  FERO Server running at {url}")
    print(f"  Press Ctrl+C to stop.")
    print(f"===================================================")

    # Open browser automatically after 0.5s
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

