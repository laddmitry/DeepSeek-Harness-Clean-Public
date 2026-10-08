# Первая публикация через GitHub Desktop

Используйте уже подготовленную папку `DeepSeek-Harness-Clean-Public`. Архив — запасная идентичная копия; распаковка не нужна. Не открывайте весь рабочий каталог с VM/логами. Перед началом прочитайте внешний PUBLICATION_READINESS_RU.md. Если там NOT READY или есть нерешённые secrets/licence/комплектность — публикацию остановить.

1. Установите [GitHub Desktop](https://desktop.github.com/), войдите в свой GitHub account через **File → Options → Accounts → Sign in**. Во вкладке **Git** проверьте имя и email: они будут публичны в commit; при желании используйте предоставленный GitHub noreply email. Для проверки нужны Python 3 и Git for Windows в PATH (это не запуск Harness).
2. Выберите **File → Add local repository… → Choose…** и подготовленную папку. Если Desktop сообщает, что это не Git repository, нажмите **create a repository here**. В создании repo задайте Name `DeepSeek-Harness-Clean-Public`, Local path — её родительскую папку, не саму папку (иначе возможна лишняя вложенность). Итоговый путь должен точно совпадать с готовой папкой. Не включайте Initialize with README; Git ignore и License — **None**, поскольку файлы уже подготовлены. Нажмите **Create repository**. Это локальное действие; удалённого repo пока нет. Desktop может сразу создать Initial commit — тогда переходите к History и проверке ниже, не создавайте искусственный второй commit.
3. В **Changes** просмотрите весь список, включая скрытые файлы. Должны быть source/packages/apps/scripts/patches/docs/kit/tests/manifests/LICENSE/notices. Не должно быть node_modules, .env с данными, worker-credentials, models, VM, test-results, logs, old .git. Щёлкайте файлы для diff. Настройки ключей не вводите. Не снимайте файлы произвольно с галочек: committed tree должен совпасть с manifest.
4. Если файлы ещё не committed: внизу слева в **Summary** напишите `Initial cleaned Harness source`, в Description — `Source distribution; limitations documented`, нажмите **Commit to main** (название ветки может отличаться). Если Changes пуст после automatic Initial commit, этот шаг уже выполнен.

### Обязательный source fixture, скрытый вложенным .gitignore

До итоговой проверки commit откройте Repository → Open in Command Prompt и выполните:

```powershell
git add -f snapshots/web/changed-files-turn/workspace.expected/app.local
```

Это синтетический файл ожидаемого результата исходного теста, а не личная настройка. В Changes включите его в первый ручной commit; если Desktop уже сделал Initial commit, создайте второй commit `Include required source fixture`. Проверять и публиковать нужно последний полный commit. Verifier допускает ранние commits только как побайтовые подмножества подготовленного набора, а выбранный commit требует полностью совпадающим. Не добавляйте force другие ignored файлы.

## ОСТАНОВИТЕСЬ ДО Publish repository

5. Перейдите в **History**, выберите созданный commit, просмотрите все файлы и изменения. Через контекстное меню **Copy SHA** получите настоящий SHA; если пункта нет, откройте **Repository → Open in Command Prompt** и выполните `git rev-parse HEAD`. Не используйте исторический operator baseline SHA.
6. В терминале из подготовленной папки выполните:

```powershell
python kit/Verify-Publication.py --commit HEAD
git status --short
git log --all --format=fuller
```

Verifier должен вывести PASS и SHA; Changes/status должны быть пустыми. Сравните SHA256 FILES.sha256.json с внешним значением из готового отчёта: `Get-FileHash FILES.sha256.json -Algorithm SHA256` в PowerShell. Для большей независимости запускайте verifier из первоначального проверенного архива/доверенной папки. Проверьте **все local commits/branches** на secrets, personal data и author metadata; первая история должна состоять только из подготовленного набора. Проверка blobs связывает новый commit с подготовленными файлами, а не объявляет его прошедшим весь старый runtime.
7. Любой FAIL, лишний файл, изменённый hash, неизвестная история, секрет или сомнение в лицензии — **не нажимать Publish repository**. Исправьте публикационную копию, обновите manifest и независимо повторите проверку. Не считайте простой delete-secret новым commit достаточным: старый secret останется в истории. Для первой публикации безопаснее создать новую чистую local history после устранения и пересканировать её. Этот набор ещё не опубликован.

## Только после проверки

8. Нажмите сверху **Publish repository**. Проверьте Name и владельца account, Organization при отсутствии организации оставьте None. **Снимите Keep this code private**, чтобы доступ был Public. Только теперь нажмите **Publish repository** в диалоге. Публикацию выполняете вы; подготовка файлов ничего не загрузила.
9. После публикации выберите **Repository → View on GitHub**. Проверьте label **Public**, затем откройте список commits и именно проверенный commit. Ссылка имеет вид `https://github.com/<owner>/<repo>/commit/<полный-проверенный-SHA>`. Скопируйте фактическую ссылку из браузера; её и отправляйте для сдачи вместе со ссылкой repo. Один main URL не фиксирует версию. Не утверждайте, что новая публикационная упаковка прошла полный NAT E2E.
10. Необязательный Release: на GitHub **Releases → Draft a new release → Choose a tag → Create new tag**. Target выберите проверенный commit SHA (если UI не позволяет, создайте tag на нём заранее), проверьте что tag ведёт именно на него. Добавьте заголовок и ограничения из LIMITATIONS_RU. Прикрепляйте только проверенный source ZIP и checksum, никаких diagnostic archives/models/VM. Нажмите **Publish release** лишь после сверки target. Для сдачи release URL можно добавить к обязательной commit URL.

Официальные инструкции: [создание repo](https://docs.github.com/en/desktop/overview/creating-your-first-repository-using-github-desktop), [публикация существующего проекта](https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-an-existing-project-to-github-using-github-desktop), [управление releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
