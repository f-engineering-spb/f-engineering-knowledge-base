# ИНСТРУКЦИЯ И КОНТЕКСТ ПРОЕКТА ДЛЯ СЛЕДУЮЩЕГО ИСКУССТВЕННОГО ИНТЕЛЛЕКТА (HANDOFF)

**Дата фиксации:** 14 сентября 2026 г.  
**Проект:** Корпоративный стиль, сайт, брендбук и чертежные стандарты **ООО «ФЕРО»** (инжиниринг, проектирование фасадов, светопрозрачных и металлических конструкций).  
**Официальный чекпоинт-коммит:** `bc6b2fb` (ветка `checkpoint/official-fero-brand-and-site`).

---

## 1. Репозиторий GitHub и контрольные ветки

* **Репозиторий:** `https://github.com/f-engineering-spb/f-engineering-knowledge-base.git`
* **Локальный путь на машине:** `C:\Users\a9379\f-engineering-knowledge-base`
* **Рабочая ветка:** `style/fero-logo-sun-guidelines-and-site-code`
* **Чекпоинт-ветка:** `checkpoint/official-fero-brand-and-site` (синхронизирована с `origin`, коммит `bc6b2fb`).

### Ключевые коммиты чекпоинта:
1. `bc6b2fb` — `feat: add calibrated 10x42mm stamp thickness test variants and A4 sheet (PNG/PDF)`
2. `44dc8e9` — `checkpoint: official fero brand style, multi-domain brandbook routing, and bilingual catalog PDF`
3. `3fb515d` — `fix: re-render all PNGs via Chrome headless for 100% SVG parity with 3D relief and fix corner stamp layout`
4. `764c993` — `feat: complete approved 3D logo, stamp, and signature suite in SVG, PNG, DXF; 100% verified download links`

---

## 2. Боевой сервер и хостинг

* **IP сервера:** `94.183.188.151:22`
* **SSH доступ:** пользователь `root`, пароль `Tpgrmklp53155615!!` (подключаться через `paramiko` в Python).
* **Корневая директория сайта:** `/var/www/ferospb.info/`
* **Директория статики:** `/var/www/ferospb.info/assets/`
* **Активный веб-адрес:** `https://ferospb.info/` (SSL Let's Encrypt настроен).
* **Целевой домен компании:** `ferospb.ru` (настроен в Nginx как алиас/зеркало).

---

## 3. Что было сделано и решено (Архитектурные исправления)

### 3.1. Устранение расхождения PNG и SVG (100% паритет рендера)
* **Проблема:** Библиотека `fitz` (PyMuPDF) и стандартные растровые движки не поддерживают расширенные фильтры SVG 2 (`feDiffuseLighting`, `feSpecularLighting`, `feMorphology`, `feDropShadow`), из-за чего на других компьютерах или вьюверах логотип отображался плоским, белым контуром на черном фоне без теней и объема.
* **Решение:** Растеризация переведена на **Google Chrome Headless** (`--headless=new`, `--force-device-scale-factor=4`, прозрачный фон `00000000`, 300 DPI). Получено 100% попиксельное совпадение: белый матовый металл, 3D-фаска, диффузный свет и мягкие двойные тени (контактная + падающая).

### 3.2. Мультидоменная маршрутизация Брендбука (исправление ошибки 404)
* **Проблема:** При переносе сайта на другой домен кнопка «Брендбук» вела на абсолютный путь или давала `Page Not Found`.
* **Решение:** Все пути в `site/index.html` и `site/brandbook/index.html` переведены на относительные (`brandbook.html` и `assets/...`). Сформирован обновленный автономный архив полного сайта для развертывания в 1 клик на любом домене:
  * URL архива: `https://ferospb.info/assets/ferospb_ru_full_site.zip` (626 МБ, HTTP 200 OK).

### 3.3. Мини-каталог (PDF)
* **Исправление:** В подвал титульного и финального листов `fero_mini_catalog.pdf` жестко прописаны оба корпоративных адреса:
  `info@ferospb.ru • www.ferospb.info • www.ferospb.ru`.
  * Файл: `https://ferospb.info/assets/fero_mini_catalog.pdf`

### 3.4. Калибровка штампа чертежа под строгие габариты 10 × 42 мм (ГОСТ Р 21.101-2020)
* **Требование пользователя:** Габариты надписи «ФЕРО» в ячейке основной надписи ($50 \times 15\text{ мм}$) должны быть **строго 10 мм по высоте и 42 мм по ширине**.
* **Параметры калибровки (при 300 DPI, $1\text{ мм} = 11{,}811\text{ px}$):**
  * Ячейка: $591 \times 177\text{ px}$ ($50 \times 15\text{ мм}$).
  * Надпись «ФЕРО»: **ровно $496 \times 118\text{ px}$ ($42{,}0 \times 10{,}0\text{ мм}$)**.
  * Отступы: по бокам по $4{,}0\text{ мм}$ ($47{,}5\text{ px}$), сверху и снизу по $2{,}5\text{ мм}$ ($29{,}5\text{ px}$).
  * В SVG: `transform="translate(250, 120) scale(1.227, 1.255)"`, шрифт `Montserrat 800`, `font-size="104px"`, `letter-spacing="5px"`.
* **Создано 5 вариантов плотности контура и теней для теста на физическом принтере:**
  1. **Вариант 1 (Базовый 100%):** контур 1.0 px ($\alpha=0.40$), тени $-1.2/+1.8$ и $-5.0/+7.0$.
  2. **Вариант 2 (+20%):** контур 1.3 px ($\alpha=0.55$), тени $-1.5/+2.2$ и $-6.0/+8.5$.
  3. **Вариант 3 (+40%):** контур 1.6 px ($\alpha=0.70$), тени $-1.8/+2.6$ и $-7.2/+10.0$.
  4. **Вариант 4 (+60%):** контур 2.0 px ($\alpha=0.82$), тени $-2.1/+3.0$ и $-8.5/+11.5$.
  5. **Вариант 5 (В 2 РАЗА / +100%):** контур 2.6 px ($\alpha=0.95$), тени $-2.6/+3.8$ и $-11.0/+14.5$.
* **Создан калибровочный лист А4 (300 DPI, $2480 \times 3508\text{ px}$):**
  * Включает физическую 50-миллиметровую шкалу сверху, все 5 вариантов в натуральную величину 1:1 с размерными линиями $42\text{ мм} \times 10\text{ мм}$ и увеличенные в $2{,}4\times$ фрагменты.
  * PDF: `https://ferospb.info/assets/fero_stamp_50x15_test_sheet_A4.pdf`
  * PNG: `https://ferospb.info/assets/fero_stamp_50x15_test_sheet_A4.png`

---

## 4. Прямые ссылки на все готовые материалы (HTTP 200 OK)

* **Калибровочный лист А4:**
  * PDF: [fero_stamp_50x15_test_sheet_A4.pdf](https://ferospb.info/assets/fero_stamp_50x15_test_sheet_A4.pdf)
  * PNG: [fero_stamp_50x15_test_sheet_A4.png](https://ferospb.info/assets/fero_stamp_50x15_test_sheet_A4.png)
* **Штампы 10 × 42 мм в ячейке 50 × 15 мм (300 DPI):**
  * [Вариант 1 (100%) PNG](https://ferospb.info/assets/fero_stamp_50x15_var1_base.png) • [SVG](https://ferospb.info/assets/fero_stamp_50x15_var1_base.svg)
  * [Вариант 2 (+20%) PNG](https://ferospb.info/assets/fero_stamp_50x15_var2_plus20.png) • [SVG](https://ferospb.info/assets/fero_stamp_50x15_var2_plus20.svg)
  * [Вариант 3 (+40%) PNG](https://ferospb.info/assets/fero_stamp_50x15_var3_plus40.png) • [SVG](https://ferospb.info/assets/fero_stamp_50x15_var3_plus40.svg)
  * [Вариант 4 (+60%) PNG](https://ferospb.info/assets/fero_stamp_50x15_var4_plus60.png) • [SVG](https://ferospb.info/assets/fero_stamp_50x15_var4_plus60.svg)
  * [Вариант 5 (В 2 раза) PNG](https://ferospb.info/assets/fero_stamp_50x15_var5_double200.png) • [SVG](https://ferospb.info/assets/fero_stamp_50x15_var5_double200.svg)
* **Официальный брендбук и каталог:**
  * [Онлайн-брендбук](https://ferospb.info/brandbook.html)
  * [Мини-каталог PDF](https://ferospb.info/assets/fero_mini_catalog.pdf)
  * [Полный архив сайта (ZIP)](https://ferospb.info/assets/fero_spb_ru_full_site.zip)

---

## 5. Правила чистоты и гигиены рабочего места

1. **Рабочий стол (`C:\Users\a9379\Desktop`):** строго запрещено сохранять временные файлы или черновики. Рабочий стол должен оставаться чистым (0 временных файлов проекта).
2. **Папка Google Диска:** `H:\Общие диски\021_F-Engineering_Knowledge_Library\03_Presentations_and_Style\Fero_style_site` — очищена от старых черновиков, содержит только утвержденный актуальный стиль.
3. **Генерация PNG:** использовать **только Chrome Headless**, избегать `fitz` (PyMuPDF) для SVG с 3D-фильтрами.

---

## 6. Следующий шаг (что делать при возобновлении сессии)

1. Узнать у пользователя, какой из 5 вариантов штампа на распечатанном тестовом листе А4 ([PDF](https://ferospb.info/assets/fero_stamp_50x15_test_sheet_A4.pdf)) дал наилучший результат на офисном принтере.
2. Принять выбранный вариант толщины за финальный эталон и при необходимости экспортировать его в чистовой угловой штамп (Форма 1/3 по ГОСТ) в форматах SVG, PNG, DXF/DWG.
3. Продолжить выполнение задач по указанию пользователя.
