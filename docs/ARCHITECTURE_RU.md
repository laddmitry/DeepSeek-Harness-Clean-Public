# Архитектура поставки

Harness состоит из Cordis plugins и внутренних workspace packages; [исходная архитектура](architecture.md) описывает состав. apps/cli загружает installation-owned base/web/headless patches. Единственный настроенный LLM provider — llm-pi-ai/local-offline через OpenAI-compatible endpoint. Windows shell runner использует отдельный worker account и sandbox-windows-acl. Kit содержит только необходимые Windows provisioning/ACL/launch scripts, без управления VM.

Цепочка будущей поставки: Harness → предоставленный пользователем совместимый endpoint. Endpoint сам может содержать downstream providers: это следует проверить при его настройке. Старый Ollama gateway не является обязательным компонентом Harness и исключён. Ollama, модели, VM, ETW/WFP-инструменты и сырые журналы не поставляются.

Код других providers, sdk-minimal, Desktop и telemetry сохранён для комплектности исходников. Сохранность пакета не означает его активацию; используйте только проверенную композицию web/headless. Произвольное embedding может активировать сохранённый DeepSeek-код.
