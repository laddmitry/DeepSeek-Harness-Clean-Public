# Очистка и изменения

Историческая инвентаризация отделила уже поставленные изменения от поздних: не все отличия можно приписывать предыдущему аудиту. [SOURCE_CHANGES.csv](SOURCE_CHANGES.csv) содержит изменения рабочего source относительно supplied candidate и оба SHA256; список не является полной историей исходного upstream.

| Файл/область | Изменение и причина |
|---|---|
| packages/bundle/base/cordis.patch.yml | Отключены DeepSeek API-key/account providers, search, extensions, session-log, inventory; sole provider local-offline. Нет штатного DeepSeek fallback |
| apps/cli/src/profile-boot.ts и packages/host/app-boot/src/profile-context.ts | Ограничен запуск web/headless и доверенными installation bundles, overlays/SDK profiles не активируются |
| packages/bundle/web-app/cordis.patch.yml и headless/cordis.patch.yml | Проверенная локальная композиция, настройки окружения/worker; installation-only configuration |
| packages/llm/llm-pi-ai и Windows sandbox/shell packages | Существующие изменения адаптера и worker support; подробные пути и хеши в CSV |

DeepSeek plugins физически сохранены в source. sdk-minimal содержит DeepSeek rows, но штатный CLI/SDK dispatch их отвергает. Product telemetry default collector сохранён в своём пакете; в проверенной web/base композиции exporter не включён. Session telemetry transport тоже сохранён; это не физическое удаление всего DeepSeek-кода.

При подготовке публикации production source не изменён. Добавлены русские документы, source configuration regression, Windows kit; README заменён коротким русским с сохранением upstream copy, .gitignore расширен, .gitattributes отключает преобразование строк ради manifest bytes. Kit provisioning адаптирован только по явному подтверждению account changes; ACL script исключает Ollama/models/tests read roots и Ollama executable/process requirements. Сам Windows runner не переписан. Новый kit не прошёл clean-install runtime.

GitHub workflows сохранены побайтово в `.github/upstream-workflows/` как исходный reference; автоматический CI/deploy/release этой поставки не активирован. Исходные tests, проверяющие upstream workflow path, после этого перемещения не подтверждены.

GitHub workflows сохранены побайтово в `.github/upstream-workflows/` как исходный reference; автоматический CI/deploy/release этой поставки не активирован. Исходные tests, проверяющие upstream workflow path, после этого перемещения не подтверждены.
