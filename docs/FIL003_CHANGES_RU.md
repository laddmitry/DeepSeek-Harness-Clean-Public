# Инструменты LOCAL_ONLY после изменения FIL-003

Произвольные PowerShell/Bash, persistent shell, terminal, PTC/runtime и workflow tool отключены в base и Web presets. Preflight перед загрузкой профиля и preset отказывает известным execution packages независимо от row ID и compatibility exemption. Для разрешённых профилей сохранён существующий запрет дополнительных overlays/bundles. PTC presentation defaults заменены на native.

Остаются файловые инструменты, поиск в workspace, in-process subagents, jobs control, задачи и цели. Фиксированные внутренние subprocess операции не являются model-facing command executor. Endpoint, pi-ai client, credentials и DeepSeek-egress ограничения не изменены. Цена ограничения: агент не может запускать команды, тесты, сборку или произвольные программы. Permission selector требует shell и отключён; FS tools используют фиксированную workspace-write политику.

Адресные raw receipts подтверждают отказ известных execution routes, реальный headless/child tool dispatch через локальный synthetic mock и разрешённые FS операции actual Web Agent. Предыдущий отчёт из 41 строки и старые compiled hashes относятся к версии до этого изменения. Полная Windows OS read isolation не заявляется.

Три EN/ZH sidecars и upgrade guide проверены отдельно. Runtime и 41-пунктовый набор при завершении документации не повторялись. Реальная модель, clean install, широкие env/UI/reboot проверки и реальные UNC shares этим исправлением не сертифицируются; DEP-001/DEP-002 остаются неисправленными.
