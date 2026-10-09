# Ранее выполненные проверки

Это обезличенная сводка отчётов HARNESS_INVENTORY_RU, DEEPSEEK_EGRESS_FINAL_RU, DEEPSEEK_REAL_RUNTIME_FINAL_RU и DEEPSEEK_NAT_RUNTIME_FINAL_RU от 8 октября 2026. Сырые журналы остаются вне публикации. Новые тесты при упаковке не запускались.

| Сценарий | Исторический результат | Граница |
|---|---|---|
| SDK/CLI: sdk-minimal и sdk отклонены | PASS | Штатный dispatch, не arbitrary embedding |
| Installation config: DeepSeek/logs/inventory отключены; env/overlay не активируют | PASS | Доверенная конфигурация стенда |
| Startup, synthetic events/feedback, shutdown | PASS | Короткий web lifecycle без browser и модели |
| Нормальный LLM запрос, отсутствие параллельной отправки | PASS | Compiled adapter → старый gateway → local mock |
| HTTP 500 | PASS | Этот же маршрут, без fallback |
| Сервер недоступен | PASS | Этот же маршрут, без fallback |
| Redirect DeepSeek | PASS | Старый gateway запрещал redirect; его здесь нет |
| Положительный контроль Node-перехвата | PASS | fetch/HTTP/TLS/socket; остановка до сети |
| Реальный headless Harness с локальной моделью | PASS | Ответ «ЛОКАЛЬНО», exit 0; внешний маршрут отключён |
| NAT: внешний маршрут, ETW, WFP контроль | PASS | Синтетический внешний TCP остановлен; событие 5157 и ETW подтверждены |
| NAT: минимальный реальный runtime | PARTIAL | Запрос достиг локального backend, DeepSeek-попыток не обнаружено; полный E2E по тайм-ауту NOT VERIFIED |
| Чистая Windows 11, новый kit/direct endpoint/browser | NOT VERIFIED | Не выполнялись для этой копии |

Семь уникальных целевых сценариев PASS; transport-control — отдельный восьмой контроль инструмента. Первоначальный config test имел resolver error и был повторён после исправления только теста. Это не production FIXED. NAT: 80 378 TCP ETW events, 472 DNS events, 279 process events, Lost=0; Node/target-WFP DeepSeek attempts=0. Некоторые сетевые metadata других PID нельзя приписывать Harness или DeepSeek.

Команда исторического driver: `node <validation-directory>/deepseek-egress-targeted.mjs <case>`; cases sdk-profile, configuration, lifecycle, success, http-error, unavailable, redirect, transport-control. Driver VM-specific и зависимый от исключённого gateway не включён как якобы воспроизводимый portable тест. Source regression [tests/deepseek-clean-config.mjs](../tests/deepseek-clean-config.mjs) добавлен для публикации; выполнение **NOT VERIFIED**, команда `node tests/deepseek-clean-config.mjs`, проверяет только текст configuration. Исходные unit tests сохранены; их наличие не доказывает запуск.

## Исправление FIL-003

Результаты выше исторические. Новые адресные результаты описаны в FIL003_CHANGES_RU.md и отдельном операторском evidence packet: model-facing execution отключён и перепроверен, FS workspace операции сохранены. Три sidecars и upgrade guide прошли scoped проверку при завершении; runtime при этом не повторялся. Остальные FAIL/BLOCKED старого 41-пунктового отчёта не отменены.
