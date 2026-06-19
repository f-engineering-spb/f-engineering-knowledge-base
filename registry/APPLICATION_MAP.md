# Карта применения правил

Статус: `Approved`

Этот файл отвечает на вопрос: какие правила читать под конкретный тип задачи.

## Универсальный порядок

Для любой новой задачи сначала читать:

1. `START_HERE.md`
2. `AGENTS.md`
3. `registry/KNOWLEDGE_REGISTRY.md`
4. `agent-instructions/F_Engineering_Interaction_Style.md`
5. этот файл

Затем подключать только нужные методики и стандарты.

## Типы задач

| Тип задачи | Признаки задачи | Core | Workflow | Style / Output | Templates | Проверки |
|---|---|---|---|---|---|---|
| Проектная рабочая папка | пользователь дает путь к новой папке проекта | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | зависит от задачи | `document-standards/Naming_and_Versioning.md` | `templates/Document_Request_Template.md` | исходники не переносить в GitHub |
| Обычная документная задача | нужно подготовить документ, письмо, записку, сводку | `agent-instructions/How_I_Work.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | нет или по смыслу | `document-standards/Document_Style_Guide.md` | `templates/Document_Request_Template.md` | структура, ясность, версия |
| HTML-документ для передачи | результат должен открываться как HTML, в том числе на телефоне | `agent-instructions/How_I_Work.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | зависит от содержания | `document-standards/HTML_Mobile_Standard.md`, `document-standards/HTML_Analytical_Report_Style.md` | `templates/HTML_Analytical_Report/` | нет горизонтального выпадения страницы, нет внешних зависимостей без необходимости |
| Самодостаточный HTML с изображениями | файл нужно отправить коллегам одним вложением | `agent-instructions/How_I_Work.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | зависит от содержания | `document-standards/HTML_Mobile_Standard.md`, `proposals/Embedded_Verification_Previews_for_HTML_Reports.md` | `templates/HTML_Analytical_Report/` | изображения встроены или поставляется вся папка; внешние CSS/JS отсутствуют |
| Аудит чертежей DWG/DXF/PDF | подсчет площадей, длин, изделий, сверка чертежей | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Engineering_Drawing_Audit/` | `document-standards/HTML_Mobile_Standard.md`, `proposals/Embedded_Verification_Previews_for_HTML_Reports.md` | `templates/Engineering_Drawing_Audit/` | статусы A/B/C/D, контрольный лист, трассировка |
| Полная фасадная спецификация для КП | из комплекта PDF/DWG/XLSX нужно получить фасадные материалы и объемы | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Complete_Facade_Commercial_Specification/`, `methodologies/Engineering_Drawing_Audit/`, `proposals/Facade_Full_Scope_Multi_Contour_Audit.md` | `document-standards/HTML_Analytical_Report_Style.md`, `document-standards/HTML_Mobile_Standard.md`, `proposals/Embedded_Verification_Previews_for_HTML_Reports.md` | `templates/Engineering_Drawing_Audit/` | матрица полноты, все фасадные контуры, проверочные превью |
| CAD-подсчет повторяемых изделий | кассеты, ламели, блоки, динамические блоки DWG/DXF | `agent-instructions/User_Working_Preferences.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Engineering_Drawing_Audit/` | расчетная таблица + HTML по необходимости | `templates/Engineering_Drawing_Audit/` | начинать с блоков/атрибутов, не выдавать зоны без подтверждения |
| Клиентская дорожная карта | план запуска, внедрения, производства, проекта | `agent-instructions/How_I_Work.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Roadmap_Information_Architecture.md` | `document-standards/Client_Roadmap_Style.md`, `document-standards/HTML_Mobile_Standard.md` | `templates/Client_Roadmap/` | контроль логики, рисков, ресурсов, финансов |
| Презентация возможностей F-Engineering | модульная презентация кейсов и сервисов | `agent-instructions/How_I_Work.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `methodologies/Roadmap_Information_Architecture.md` | `document-standards/Document_Style_Guide.md`, `document-standards/HTML_Mobile_Standard.md`, `document-standards/HTML_Analytical_Report_Style.md` | по проектной папке презентаций | кейс должен показывать вход, обработку, результат, проверку |
| Google Docs / Google Sheets работа | пользователь просит править документы или таблицы Google | `agent-instructions/User_Working_Preferences.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | отдельная методика пока не утверждена | стиль зависит от результата | нет | работать в нативных Google Docs/Sheets, исходные Word/Excel не портить |
| Фото/видео оборудования в спецификацию | по фото или видео нужно собрать состав оборудования, станков, узлов | `agent-instructions/How_I_Work.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | методика пока отсутствует, создать proposal после пилота | Excel/Google Sheets + HTML при необходимости | нет | фиксировать источник кадра/фото, уверенность распознавания, вопросы |
| Финансовые Google-таблицы | FINDEX, кошельки, движение денежных средств | `agent-instructions/User_Working_Preferences.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | методика пока отсутствует, использовать проектные правила Google_Tools как справку | Google Sheets, HTML-описание по необходимости | нет | проверять формулы, связи, двойную запись, права доступа |
| Новый чат / перенос настроения работы | пользователь начинает новый проект и хочет сохранить манеру общения из предыдущего чата | `agent-instructions/F_Engineering_Interaction_Style.md`, `agent-instructions/How_I_Work.md` | зависит от проекта | зависит от результата | нет | не менять базовые правила общения без явного указания; отличать стиль общения от стиля документа |

## Если подходящего типа задачи нет

1. Применить core-правила.
2. Выбрать style-стандарт под нужный формат результата.
3. Выполнить задачу в проектной папке.
4. Если получился повторяемый успешный подход, оформить предложение в `proposals/`.
