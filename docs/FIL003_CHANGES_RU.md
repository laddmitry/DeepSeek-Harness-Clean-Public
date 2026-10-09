# Инструменты LOCAL_ONLY после изменения FIL-003

Произвольные PowerShell/Bash, persistent shell, terminal, PTC/runtime и workflow tool отключены в base и Web presets. Preflight перед загрузкой профиля и preset отказывает известным execution packages независимо от row ID и compatibility exemption. Для разрешённых профилей сохранён существующий запрет дополнительных overlays/bundles. PTC presentation defaults заменены на native.

Остаются файловые инструменты, поиск в workspace, in-process subagents, jobs control, задачи и цели. Фиксированные внутренние subprocess операции не являются model-facing command executor. Endpoint, pi-ai client, credentials и DeepSeek-egress ограничения не изменены. Цена ограничения: агент не может запускать команды, тесты, сборку или произвольные программы. Permission selector требует shell и отключён; FS tools используют фиксированную workspace-write политику.

Результаты исправленного runtime ещё должны быть подтверждены отдельными raw receipts. Предыдущий отчёт из 41 строки и старые compiled hashes относятся к версии до этого изменения. Полная Windows OS read isolation не заявляется.
