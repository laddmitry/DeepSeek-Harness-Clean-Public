# Публикация исправления FIL-003 через GitHub Desktop

Используйте подготовленную отдельную папку DeepSeek-Harness-Clean-Public-FIL003. ZIP содержит то же source tree без Git metadata; для сохранения проверенного commit используйте папку, архив распаковывать не нужно. В папке уже есть локальный репозиторий и commit: создавать новый repository или первый commit не требуется.

1. В GitHub Desktop выберите File → Add Local Repository → Choose и укажите готовую папку. Нажмите Add Repository.
2. Проверьте Current Repository и Current Branch: исправление находится в fix/fil003-local-only. Не переключайтесь на main и не копируйте файлы поверх старой публикационной папки.
3. В Changes должно быть No local changes. В History выберите последний commit, просмотрите изменённые файлы; правой кнопкой → Copy SHA. Полный SHA должен совпасть с отдельным отчётом поставки.
4. Через Repository → Repository settings → Remote проверьте URL https://github.com/laddmitry/DeepSeek-Harness-Clean-Public.git. В Git config остаётся выбранный GitHub noreply.

## Остановитесь перед Publish branch / Push origin

5. Сверьте SHA, список файлов и ограничения. При необходимости в Repository → Open in Command Prompt выполните git status --short и git rev-parse HEAD. Проверяйте секреты и author metadata отдельно от файлового manifest. Старый kit verifier не используйте; текущий Verify-Publication.py сравнивает target с новым FILES.sha256.json, не объявляя исторические версии испорченными.
6. Не называйте source-only комплект окончательным релизом или полным LOCAL_ONLY PASS: DEP-001/DEP-002 не исправлены, clean install и ряд runtime критериев не проверены. Если обнаружились лишние файлы, секреты или несовпадения — остановитесь.
7. Только после просмотра нажмите Publish branch либо Push origin для fix/fil003-local-only. Это загрузит отдельную ветку существующего публичного репозитория. Main не меняйте; merge/release не выполняются этой инструкцией.
8. Выберите Repository → View on GitHub, откройте опубликованную ветку и commit. Для сдачи отправляйте https://github.com/laddmitry/DeepSeek-Harness-Clean-Public/commit/ПОЛНЫЙ_SHA_ИЗ_ОТЧЁТА. До вашего push эта новая ссылка не считается опубликованной.

Если отображается Publish repository вместо ожидаемой ветки существующего remote, сначала проверьте выбранную папку и Remote. Не создавайте автоматически новый repo и не публикуйте main.

Официальные инструкции: [добавление локального репозитория](https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop), [управление и публикация ветки](https://docs.github.com/en/desktop/making-changes-in-a-branch/managing-branches-in-github-desktop).
