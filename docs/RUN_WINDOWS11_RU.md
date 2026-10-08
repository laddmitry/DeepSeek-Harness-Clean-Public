# Запуск и собственный LLM endpoint

Штатный запуск очищенной поставки: `dsh` с профилем web или headless. Kit вызывает собранный официальный `apps/cli/lib/bin.js`, не отдельный plugin entry. Запускайте в обычной DSHAudit-сессии после установки.

```powershell
& C:\DSH\kit\Run-Harness.ps1 -Profile web
# Для минимальной синтетической задачи при наличии backend:
& C:\DSH\kit\Run-Harness.ps1 -Profile headless -Task 'Ответь одним словом: ТЕСТ'
```

Остановить: Ctrl+C в этом окне. Browser flow этой поставки полностью не проверен. Не делайте task с настоящими данными до проверки выбранного backend и политики его redirects/fallback.

В `packages/bundle/base/cordis.patch.yml`, в provider `local-offline`, используются `api: openai-completions`, `baseURL: http://127.0.0.1:8000/v1`, `apiKeyEnv: LOCAL_MODEL_API_KEY`, model `local-model`. Порт 8000 раньше обслуживал отдельный Ollama gateway; его здесь нет. Никакой сервер на этом порту комплектом не запускается.

Для будущего собственного OpenAI-совместимого backend администратор установки меняет только baseURL и id модели в этом доверенном installation patch **до сборки**, согласует `agent-default-model.model` с новым id и затем пересобирает. Имя provider можно оставить `local-offline`. Адрес и model id берутся у владельца backend; значения здесь не придуманы. Если сервер требует ключ, задайте LOCAL_MODEL_API_KEY только в локальном окружении контроллера. Не записывайте его в source, docs, командную строку или Git. Настройки пользователя, overlay patches и settings UI в очищенной конфигурации не служат обходным путём: они отключены/ограничены.

После изменения endpoint прежние runtime PASS на новый маршрут не распространяются. Нужны короткие synthetic проверки normal/error/no-fallback и redirect, с остановкой обращений DeepSeek до сети. Прежний redirect PASS обеспечивал исключённый Ollama gateway (`redirect:'error'`); прямой generic LLM transport может вести себя иначе. Такой будущий маршрут сейчас **NOT VERIFIED**. Не публикуйте адаптацию как проверенную на вашем сервере.
