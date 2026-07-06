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
8. `docs/F_ENGINEERING_VISUAL_STYLE.md`, если задача создаёт или изменяет визуальные артефакты

Затем подключать только нужные модули и служебные правила.

## Типы задач

| Тип задачи | Признаки задачи | Core | Workflow / Module | Style / Output | Проверки |
|---|---|---|---|---|---|
| Проектная рабочая папка | пользователь дает путь к новой папке проекта | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | зависит от задачи | зависит от результата | исходники не переносить в GitHub; русские пути и файлы читаются как UTF-8 |
| Новый бизнес-модуль | пользователь описывает повторяемую автоматизацию, которую нужно сохранить как кирпичик процесса | `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md`, `docs/GitHub_Knowledge_Base_Workflow.md` | `business-processes/MODULE_STANDARD.md`, `business-processes/MODULE_REGISTRY.md`, `business-processes/PROCESS_MAP.md` | `docs/F_ENGINEERING_VISUAL_STYLE.md`, если есть визуальный результат | модуль должен иметь вход, выход, пользователей, боль, стадии применения, инструкцию оператору и критерии готовности |
| Карта бизнес-процессов | нужно понять, где отдельные модули подключаются к стадиям компании | `agent-instructions/F_Engineering_Interaction_Style.md` | `business-processes/PROCESS_MAP.md`, `business-processes/MODULE_REGISTRY.md` | Markdown / схема по необходимости | не строить монолит до проверки кирпичиков; один модуль может применяться в нескольких стадиях |
| Первичная индексация входящей документации | от заказчика поступил ворох папок, PDF, DWG и других файлов; нужно понять состав, создать реестр, сущности и быстрый навигатор | `agent-instructions/Project_Workspace_AGENTS.md`, `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | `business-processes/modules/incoming-documentation-indexer/`, `business-processes/MODULE_STANDARD.md`, `business-processes/PROCESS_MAP.md` | `docs/F_ENGINEERING_VISUAL_STYLE.md`, если создается HTML / Apps Script просмотрщик | не переносить клиентские файлы в GitHub; сначала собрать сырой реестр, затем определить сущности; не перегружать просмотрщик лишними фильтрами; пройти `quality-checklist.md` |
| Google Docs / договоры | нужно править договоры или документы в Google Docs с контролем текста, форматирования и проверки | `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md`, `agent-instructions/User_Working_Preferences.md` | `document-processing/google-docs/Google_Docs_Workflow_Index.md` | `docs/F_ENGINEERING_VISUAL_STYLE.md`, если создается выдаваемый документ | работать в нативных Google Docs, не портить исходные Word/Excel, проверять правки и итоговую структуру |
| Визуальный артефакт | создается HTML, Markdown, Google Sheet, презентация, отчет или КП | `agent-instructions/Cyrillic_UTF8_Handling.md`, `agent-instructions/F_Engineering_Interaction_Style.md` | зависит от бизнес-задачи | `docs/F_ENGINEERING_VISUAL_STYLE.md` | не использовать старые разрозненные стили; DS-010 является источником истины |
| Новый чат / перенос рабочей манеры | пользователь начинает новый проект и хочет сохранить манеру общения из предыдущего чата | `agent-instructions/F_Engineering_Interaction_Style.md`, `agent-instructions/How_I_Work.md`, `agent-instructions/Cyrillic_UTF8_Handling.md` | зависит от проекта | зависит от результата | не менять базовые правила общения без явного указания; отличать стиль общения от стиля документа; не ломать кириллицу |

## Если подходящего типа задачи нет

1. Применить core-правила.
2. Если есть русский текст, кириллические пути или Windows/PowerShell, применить `agent-instructions/Cyrillic_UTF8_Handling.md`.
3. Если задача требует сохранить рабочую манеру F-Engineering, применить `agent-instructions/F_Engineering_Interaction_Style.md`.
4. Если результат визуальный, применить `docs/F_ENGINEERING_VISUAL_STYLE.md`.
5. Выполнить задачу в проектной папке.
6. Если получился повторяемый успешный подход, оформить новый бизнес-модуль в `business-processes/modules/` или служебный модуль в соответствующем разделе.
