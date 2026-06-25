# Реестр действующих знаний

Реестр является быстрым указателем утвержденных материалов базы знаний.
Источником действующей версии каждого материала является ветка `main`.

| ID | Материал | Тип | Раздел | Назначение | Применять когда | Статус |
|---|---|---|---|---|---|---|
| GV-001 | `governance/Knowledge_Governance.md` | Core | Управление знаниями | Порядок ведения базы знаний, статусы и приоритеты | Всегда при добавлении или выборе правил | Approved |
| RG-001 | `registry/APPLICATION_MAP.md` | Core | Реестры | Карта применения правил по типам задач | Перед началом новой задачи | Approved |
| RG-002 | `registry/BRANCH_REGISTRY.md` | Core | Реестры | Реестр экспериментальных веток и направлений | При создании ветки с новым правилом | Approved |
| RG-003 | `registry/RULE_CONFLICTS.md` | Core | Реестры | Известные конфликты правил и решения | Когда правила пересекаются или спорят | Approved |
| AG-001 | `agent-instructions/Project_Workspace_AGENTS.md` | Core | Инструкции агентам | Организация работы в проектной папке | При работе в проектной папке | Approved |
| AG-002 | `agent-instructions/How_I_Work.md` | Core | Инструкции агентам | Порядок постановки и выполнения документных задач | Для большинства документных задач | Approved |
| AG-003 | `agent-instructions/User_Working_Preferences.md` | Core | Инструкции агентам | Подтвержденные предпочтения пользователя | При выборе формата результата и подхода к работе | Approved |
| AG-004 | `agent-instructions/Codex_Desktop_State_Sync_and_Recovery.md` | Core | Инструкции агентам | Синхронизация проектов и чатов между компьютерами, резервирование и аварийное восстановление Codex Desktop | Только при задачах синхронизации Codex Desktop | Candidate |
| AG-005 | `agent-instructions/Cyrillic_UTF8_Handling.md` | Core | Инструкции агентам | Правила чтения, записи и проверки кириллицы и UTF-8 без mojibake | Всегда при работе с русским текстом, кириллическими путями, Windows/PowerShell, GitHub Markdown, HTML, CSV, JSON и документными артефактами | Approved |
| AG-006 | `agent-instructions/F_Engineering_Interaction_Style.md` | Core | Инструкции агентам | Стиль общения и рабочая манера Codex в проектах F-Engineering | При старте нового чата, нового проекта или требует сохранить рабочую манеру F-Engineering | Review |
| AG-006 | `agent-instructions/F_Engineering_Interaction_Style.md` | Core | Инструкции агентам | Стиль общения и рабочая манера Codex в проектах F-Engineering | При старте нового чата, нового проекта или восстановлении настроения работы | Review |
| AG-007 | `agent-instructions/F_Engineering_Shared_Drive_Workspace.md` | Core | Инструкции агентам | Использование общего диска F-Engineering как основной проектной рабочей области и зеркала базы знаний | При работе в проектах на `H:\Общие диски\022-F_engineering` или при настройке нового проекта F-Engineering | Candidate |
| DS-001 | `document-standards/Document_Style_Guide.md` | Style | Стандарты документов | Общий визуальный и структурный стиль | Для оформляемых документов | Approved |
| DS-002 | `document-standards/Naming_and_Versioning.md` | Core | Стандарты документов | Именование файлов и версии | Для всех создаваемых файлов | Approved |
| DS-003 | `document-standards/HTML_Mobile_Standard.md` | Style | Стандарты документов | Адаптивность HTML для мобильных экранов | Для всех HTML-файлов | Approved |
| DS-004 | `document-standards/HTML_Analytical_Report_Style.md` | Style | Стандарты документов | Оформление аналитических HTML-отчетов | Для аналитических HTML, отчетов, спецификаций | Approved |
| DS-005 | `document-standards/Client_Roadmap_Style.md` | Style | Стандарты документов | Оформление клиентских дорожных карт | Для дорожных карт и планов запуска | Approved |
| DS-006 | `proposals/Embedded_Verification_Previews_for_HTML_Reports.md` | Style | Стандарты документов | Встроенные проверочные превью в HTML-отчётах | Для HTML с расчетами, объемами и проверкой | Approved |
| DS-007 | `document-standards/F_Engineering_Logo_Standard.md` | Style | Стандарты документов | Единый логотипный блок F-Engineering / Facade engineering group | Для всех HTML, КП, презентаций и клиентских документов | Review |
| DS-008 | `document-standards/Black_White_Minimalist_Document_Style.md` | Style | Стандарты документов | Черно-белая минималистичная стилистика документов | По умолчанию для большинства коммерческих и управленческих документов | Review |
| MT-001 | `methodologies/Roadmap_Information_Architecture.md` | Workflow | Методики | Смысловая декомпозиция и построение дорожных карт | Для дорожных карт, презентаций, планов запуска | Approved |
| MT-002 | `methodologies/Engineering_Drawing_Audit/` | Workflow | Методики | Аудит чертежей и подсчет объемов | Для DWG/DXF/PDF, чертежей, подсчета объемов | Approved |
| MT-003 | `proposals/Facade_Full_Scope_Multi_Contour_Audit.md` | Workflow | Методики | Полный многоконтурный аудит фасадных конструкций | Для фасадных конструкций и коммерческих предложений | Approved |
| MT-004 | `methodologies/Complete_Facade_Commercial_Specification/` | Workflow | Методики | Полная проверяемая фасадная спецификация для коммерческого предложения | Когда нужен итоговый фасадный состав работ и объемов | Approved |
| MT-005 | `methodologies/Mark_Based_Drawing_Audit/` | Workflow | Методики | Марочный аудит чертежей: полный словарь обозначений, листы по маркам, объемы, источники и комментарии | Когда нужно расшифровать все марки/обозначения и подготовить проверяемую базу объемов для КП, спецификации или Google Sheets | Candidate |
| TP-001 | `templates/Document_Request_Template.md` | Template | Шаблоны | Постановка задачи на документ | Когда нужно оформить задачу на документ | Approved |
| TP-002 | `templates/Client_Roadmap/` | Template | Шаблоны | Эталон клиентской дорожной карты | Для дорожных карт | Approved |
| TP-003 | `templates/Engineering_Drawing_Audit/` | Template | Шаблоны | Постановка задачи на аудит чертежей | Для аудита чертежей | Approved |
| TP-004 | `templates/HTML_Analytical_Report/` | Template | Шаблоны | Эталон аналитического HTML-отчета | Для аналитических HTML-документов | Approved |
| TL-001 | `tools/estimate_scope/` | Tool | Инструменты | Извлечение компактного реестра работ и объемов из Excel-смет, ВОР и Grand-Smeta XLSX-экспортов | Когда нужно понять состав работ, объемы, фасадные группы, основу для ДДС или последующей проверки по чертежам | Candidate |
| TL-002 | `tools/estimate_scope/extract_grand_smeta_full_rows.py` | Tool | Инструменты | Полная построчная выгрузка Grand-Smeta/XLSX-смет с сохранением родительских позиций, ресурсов, НР/СП и итогов | Когда нужно доказательно показать состав сметы и не спутать ресурсные строки с самостоятельными работами | Candidate |

Статус `Approved` присвоен после объединения Pull Request №2 с веткой `main`.

Стандарты `DS-007` и `DS-008` добавлены в ветке `style/black-white-minimalist-documents` и получают статус `Approved` после объединения соответствующего Pull Request с `main`.

Стандарт `AG-006` добавлен в ветке `style/interaction-tone-f-engineering` и получает статус `Approved` после объединения соответствующего Pull Request с `main`.

Методика `MT-005` добавлена в ветке `methodology/mark-based-drawing-audit` и получает статус `Approved` после объединения соответствующего Pull Request с `main`.
Инструмент `TL-002` добавлен в ветке `codex/grand-smeta-full-rows-utf8` и получает статус `Approved` после проверки и объединения соответствующего Pull Request с `main`.
