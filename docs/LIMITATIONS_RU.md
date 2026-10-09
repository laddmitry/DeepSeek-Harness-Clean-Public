# Ограничения

Исторические PASS относятся к конкретным наблюдавшимся сценариям. Полный NAT E2E завершился тайм-аутом. Не подтверждены все browser/workers/длительный простой, произвольное embedding, все возможные конфигурации и абсолютное отсутствие утечек.

Ollama-specific gateway исключён. Его redirect PASS не переносится на generic прямой endpoint. Нового backend пока нет; ответы без inference не обещаются. Изменение endpoint требует повторной точечной проверки этого маршрута, включая redirect и server-side fallback. Старый runtime не сертифицирует новый commit целиком.

Новые Windows kit scripts и установка именно этой копии на чистую Windows 11 — NOT VERIFIED. Dependencies скачиваются отдельно; чужие licences/terms сохраняются. Source-only комплект не содержит proprietary platform binaries. Нативные/desktop dependencies могут иметь дополнительные требования при последующей сборке, не заявленные как проверенные для любого компьютера.

Исходные upstream replay snapshots и fixtures — часть тестового дерева, не VirtualBox snapshots; не удалены ради внешнего сходства названий. Документы upstream описывают и отключённые здесь режимы. Новые русские инструкции задают область поставки; все существующие upstream документационные ссылки и multilingual gates заново не проверялись.

Upstream workflow definitions сохранены вне активного workflows-каталога. Некоторые исходные CI-layout tests ожидают прежние пути; их PASS для этой упаковки не заявляется.

Upstream workflow definitions сохранены вне активного workflows-каталога. Некоторые исходные CI-layout tests ожидают прежние пути; их PASS для этой упаковки не заявляется.

## LOCAL_ONLY: чтение файлов и произвольное исполнение

Windows ACL sandbox ограничивает запись, но оставляет чтение доступным. Режим `workspace-write` и `WRITE_RESTRICTED` не обеспечивают конфиденциальность файлов вне workspace. В этой рабочей версии отключены model-facing PowerShell/Bash, persistent terminal, PTC и workflow исполнения; файловые `read`, `write`, `edit`, поиск и in-process subagents сохраняются. Preset preflight отказывает известным execution providers/consumers до импорта, включая повторное включение в вложенной группе или через alias. Profile/home/CLI overlays и дополнительные bundle layers остаются запрещёнными существующим launcher.

Это ограничение состава инструментов, а не новое OS-level запрещение чтения. Нативный subprocess service сохраняется для фиксированных внутренних операций Harness и поиска; он не предоставлен модели как произвольный executor. Изменённые installation files и сторонние плагины за пределами разрешённой композиции не входят в эту гарантию. Исторические PASS прежней версии не сертифицируют новый runtime. До адресной проверки `FIL-003` остаётся FAIL; итог и точные evidence будут в отдельном `FIL003_FIX_AND_RETEST_RU.md`.

Permission selector, зависящий от shell service, явно отключён. Сохраняется фиксированная политика workspace-write для FS tools; смена режима через этот selector недоступна. Чтение реального UNC share не подтверждено: тестовый несуществующий localhost share вернул ECONNRESET, а не доказанный OS-deny. Фактический shell/terminal/native-child запуск отключён до dispatch.
