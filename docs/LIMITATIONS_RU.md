# Ограничения

Исторические PASS относятся к конкретным наблюдавшимся сценариям. Полный NAT E2E завершился тайм-аутом. Не подтверждены все browser/workers/длительный простой, произвольное embedding, все возможные конфигурации и абсолютное отсутствие утечек.

Ollama-specific gateway исключён. Его redirect PASS не переносится на generic прямой endpoint. Нового backend пока нет; ответы без inference не обещаются. Изменение endpoint требует повторной точечной проверки этого маршрута, включая redirect и server-side fallback. Старый runtime не сертифицирует новый commit целиком.

Новые Windows kit scripts и установка именно этой копии на чистую Windows 11 — NOT VERIFIED. Dependencies скачиваются отдельно; чужие licences/terms сохраняются. Source-only комплект не содержит proprietary platform binaries. Нативные/desktop dependencies могут иметь дополнительные требования при последующей сборке, не заявленные как проверенные для любого компьютера.

Исходные upstream replay snapshots и fixtures — часть тестового дерева, не VirtualBox snapshots; не удалены ради внешнего сходства названий. Документы upstream описывают и отключённые здесь режимы. Новые русские инструкции задают область поставки; все существующие upstream документационные ссылки и multilingual gates заново не проверялись.

Upstream workflow definitions сохранены вне активного workflows-каталога. Некоторые исходные CI-layout tests ожидают прежние пути; их PASS для этой упаковки не заявляется.

Upstream workflow definitions сохранены вне активного workflows-каталога. Некоторые исходные CI-layout tests ожидают прежние пути; их PASS для этой упаковки не заявляется.
