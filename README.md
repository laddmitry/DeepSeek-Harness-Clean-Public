# Очищенный DeepSeek Harness

Исходная поставка агентного Harness: внутренние пакеты, конфигурации, сборочные scripts, patches, тесты и документация. В проверенной композиции отключены DeepSeek providers, account, поиск, session logs и inventory; запуск ограничен web/headless и installation patches.

**Ollama и языковых моделей в комплекте нет.** Нужен отдельно предоставляемый совместимый LLM backend. Адрес собственного сервера пока не настроен. Оставленный endpoint `http://127.0.0.1:8000/v1` — прежнее локальное значение, а не поставляемый сервер.

Ранее подтверждены 7 целевых сценариев, локальный реальный запуск, контроль ETW/WFP при NAT. Полный NAT E2E завершился тайм-аутом; новый прямой endpoint, browser runtime и установка этой копии на чистую Windows 11 — NOT VERIFIED. Отсутствие наблюдавшихся запросов не означает абсолютной гарантии.

Начните с [установки](docs/INSTALL_WINDOWS11_RU.md), [документации](docs/README.md) и [ограничений](docs/LIMITATIONS_RU.md). Результаты и происхождение: [проверки](docs/VERIFICATION_RU.md). Исходный README сохранён как [README_UPSTREAM.md](README_UPSTREAM.md); его штатные инструкции могут описывать отключённые здесь профили.

Лицензия [MIT](LICENSE), copyright DeepSeek сохранён. [Third-party notices](THIRD_PARTY_NOTICES.md) и вложенные лицензии обязательны. Это изменённая поставка, не официальный релиз DeepSeek.
