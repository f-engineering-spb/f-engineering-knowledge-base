# Карта применения правил

Статус: `Approved`

Этот файл отвечает на вопрос: какие правила читать под конкретный тип задачи.

## Универсальный порядок

Для любой новой задачи сначала читать:

1. `START_HERE.md`
2. `AGENTS.md`
3. `registry/KNOWLEDGE_REGISTRY.md`
4. этот файл
5. `agent-instructions/Cyrillic_UTF8_Handling.md`, если задача содержит русский текст, кириллические пути, Windows/PowerShell, GitHub Markdown, HTML, CSV, JSON или документные артефакты
6. `agent-instructions/F_Engineering_Interaction_Style.md`, если задача запускает новый чат, новый проект или требует сохранить рабочую манеру F-Engineering
7. `docs/GitHub_Knowledge_Base_Workflow.md`, если задача добавляет, меняет, утверждает или проверяет знание в GitHub-базе

Затем подключать только нужные методики и стандарты.

## Типы задач

| Тип задачи | Признаки задачи | Core | Workflow | Style / Output | Templates | Проверки |
|---|---|---|---|---|---|---|
| Проектная рабочая папка | пользователь дает путь к новой папке проекта | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | зависит от задачи | `document-standards/Naming_and_Versioning.md` | `templates/Document_Request_Template.md` | исходники не переносить в GitHub; русские файлы читаются как UTF-8 |
| Обычная документная задача | нужно подготовить документ, письмо, записку, сводку | `agent-instructions/How_I_Work.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | нет или по смыслу | `document-standards/Document_Style_Guide.md` | `templates/Document_Request_Template.md` | структура, ясность, версия, отсутствие mojibake |
| HTML-документ для передачи | результат должен открываться как HTML, в том числе на телефоне | `agent-instructions/How_I_Work.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | зависит от содержания | `document-standards/HTML_Mobile_Standard.md`, `document-standards/HTML_Analytical_Report_Style.md` | `templates/HTML_Analytical_Report/` | нет горизонтального выпадения страницы, нет внешних зависимостей без необходимости, есть `<meta charset="utf-8">` |
| Самодостаточный HTML с изображениями | файл нужно отправить коллегам одним вложением | `agent-instructions/How_I_Work.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | зависит от содержания | `document-standards/HTML_Mobile_Standard.md`, `proposals/Embedded_Verification_Previews_for_HTML_Reports.md` | `templates/HTML_Analytical_Report/` | изображения встроены или поставляется вся папка; внешние CSS/JS отсутствуют; есть `<meta charset="utf-8">` |
| Аудит чертежей DWG/DXF/PDF | подсчет площадей, длин, изделий, сверка чертежей | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Engineering_Drawing_Audit/` | `document-standards/HTML_Mobile_Standard.md`, `proposals/Embedded_Verification_Previews_for_HTML_Reports.md` | `templates/Engineering_Drawing_Audit/` | статусы A/B/C/D, контрольный лист, трассировка, корректная кириллица в путях и отчетах |
| Полная фасадная спецификация для КП | из комплекта PDF/DWG/XLSX нужно получить фасадные материалы и объемы | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Complete_Facade_Commercial_Specification/`, `methodologies/Engineering_Drawing_Audit/`, `proposals/Facade_Full_Scope_Multi_Contour_Audit.md` | `document-standards/HTML_Analytical_Report_Style.md`, `document-standards/HTML_Mobile_Standard.md`, `proposals/Embedded_Verification_Previews_for_HTML_Reports.md` | `templates/Engineering_Drawing_Audit/` | матрица полноты, все фасадные контуры, проверочные превью, корректная кириллица в источниках и HTML |
| Сметы, ВОР и состав работ | есть Excel-сметы, локальные сметы, объектные сметы, Grand-Smeta XLSX/GGE/GSFX, нужно понять объемы работ перед КП/ДДС/верификацией | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `tools/estimate_scope/`, затем по необходимости `methodologies/Engineering_Drawing_Audit/` | Google Sheets или Excel-реестр + аналитическая записка по необходимости | нет | не переносить клиентские сметы в GitHub; сохранять трассировку файл/лист/строка; разделять сметные, авторские и расчетные объемы; проверять кириллицу в Excel/CSV |
| CAD-подсчет повторяемых изделий | кассеты, ламели, блоки, динамические блоки DWG/DXF | `agent-instructions/User_Working_Preferences.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Engineering_Drawing_Audit/` | расчетная таблица + HTML по необходимости | `templates/Engineering_Drawing_Audit/` | начинать с блоков/атрибутов, не выдавать зоны без подтверждения, не ломать кириллические имена слоев/блоков |
| Клиентская дорожная карта | план запуска, внедрения, производства, проекта | `agent-instructions/How_I_Work.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Roadmap_Information_Architecture.md` | `document-standards/Client_Roadmap_Style.md`, `document-standards/HTML_Mobile_Standard.md` | `templates/Client_Roadmap/` | контроль логики, рисков, ресурсов, финансов, отсутствие mojibake |
| Презентация возможностей F-Engineering / сложная смысловая презентация | модульная презентация кейсов и сервисов; клиентский питч; презентация модели взаимодействия; несколько конкурирующих акцентов; пользователь хочет сначала согласовать логику | `agent-instructions/How_I_Work.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Presentation_Logic_First_Creation.md`, затем по необходимости `methodologies/Roadmap_Information_Architecture.md` | `document-standards/Document_Style_Guide.md`, `document-standards/HTML_Mobile_Standard.md`, `document-standards/HTML_Analytical_Report_Style.md` | по проектной папке презентаций | сначала утвердить главный тезис, блоки, функцию каждого слайда и текстовую блок-схему; не делать HTML/PPTX до согласования логики; кейсы и картинки использовать только в заранее определенной роли; русские подписи читаются корректно |
| Google Docs / Google Sheets работа | пользователь просит править документы или таблицы Google | `agent-instructions/User_Working_Preferences.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Mark_Based_Drawing_Audit/`, если Google Sheets используется для реестра марок, объемов и источников | для рабочих таблиц применять черно-белое оформление без темных шапок и цветных плашек | нет | работать в нативных Google Docs/Sheets, исходные Word/Excel не портить, числовые колонки должны суммироваться, не переносить битый экспорт в рабочий документ |
| Фото/видео оборудования в спецификацию | по фото или видео нужно собрать состав оборудования, станков, узлов | `agent-instructions/How_I_Work.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | методика пока отсутствует, создать proposal после пилота | Excel/Google Sheets + HTML при необходимости | нет | фиксировать источник кадра/фото, уверенность распознавания, вопросы, русские названия не искажены |
| Финансовые Google-таблицы | FINDEX, кошельки, движение денежных средств | `agent-instructions/User_Working_Preferences.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | методика пока отсутствует, использовать проектные правила Google_Tools как справку | Google Sheets в простой черно-белой рабочей стилистике; HTML-описание по необходимости | нет | проверять формулы, связи, двойную запись, права доступа, не ломать русские категории и счета; не использовать темные шапки с белым текстом |
| Новый чат / перенос настроения работы | пользователь начинает новый проект и хочет сохранить манеру общения из предыдущего чата | `agent-instructions/F_Engineering_Interaction_Style.md`, `agent-instructions/How_I_Work.md`, `agent-instructions/Cyrillic_UTF8_Handling.md` | зависит от проекта | зависит от результата | нет | не менять базовые правила общения без явного указания; отличать стиль общения от стиля документа; не ломать кириллицу |

## Если подходящего типа задачи нет

1. Применить core-правила.
2. Если есть русский текст, кириллические пути или Windows/PowerShell, применить `agent-instructions/Cyrillic_UTF8_Handling.md`.
3. Если задача требует сохранить рабочую манеру F-Engineering, применить `agent-instructions/F_Engineering_Interaction_Style.md`.
4. Выбрать style-стандарт под нужный формат результата.
5. Выполнить задачу в проектной папке.
6. Если получился повторяемый успешный подход, оформить предложение в `proposals/`.
