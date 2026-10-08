# Установка на Windows 11

Процедура этой публикационной копии на совершенно чистой Windows 11: **NOT VERIFIED**. Ранее сборка и запуск подтверждены в подготовленной Windows 11 VM. Новые установочные scripts адаптированы из её provisioning; не выдавайте их за проверенный установщик.

1. Нужны Windows 11 x64, права администратора для создания выделенных локальных accounts, свободное место для зависимостей и сборки. Установите [Node.js](https://nodejs.org/en/download) (ранее использован 24.21.0; engines: ^22.19.0 или >=24), [PowerShell 7](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-windows), [Git for Windows](https://git-scm.com/downloads/win). Package manager строго `pnpm@11.28.5` из package.json: `npm install -g pnpm@11.28.5`. Для нативных зависимостей при отсутствии готового бинарного пакета могут понадобиться Python 3 и Visual Studio Build Tools с Desktop development with C++; см. [node-gyp](https://github.com/nodejs/node-gyp#on-windows). Бинарные зависимости скачиваются package manager отдельно и имеют собственные лицензии.
2. После публикации на странице конкретного проверенного commit используйте **Code → Download ZIP**, распакуйте. Не скачивайте произвольный поздний main вместо проверенного SHA. В администраторском PowerShell 7 создайте `C:\DSH\source` и скопируйте содержимое исходной папки в `C:\DSH\source\deepseek-harness-master`. Используйте новую отдельную установку, не перезаписывайте существующий C:\DSH. Это путь поставки, а не личный путь прежнего компьютера.
3. До сборки настройте доверенный `packages/bundle/base/cordis.patch.yml` по [инструкции endpoint](RUN_WINDOWS11_RU.md). Не включайте DeepSeek plugins. Без backend сборка возможна, генерация ответов невозможна.
4. В папке исходников выполните:

```powershell
node --version
pnpm --version
pnpm install --frozen-lockfile
pnpm run build
```

Не используйте `pnpm update` и не исправляйте lockfile автоматически. Если frozen install или build завершается ошибкой, остановитесь и сохраните ошибку; такая установка не подтверждена. Ранее эти команды прошли на подготовленном стенде, это не новый запуск данного архива.

5. В администраторском PowerShell 7 подготовьте стандартную структуру (Node должен находиться в `C:\Program Files\nodejs\node.exe`, как ожидает ACL script):

```powershell
$source='C:\DSH\source\deepseek-harness-master'
New-Item -ItemType Directory -Force C:\DSH\kit,C:\DSH\tools,C:\DSH\workspace,C:\DSH\data\temp,C:\DSH\logs | Out-Null
Copy-Item -Path "$source\kit\*" -Destination C:\DSH\kit
$controllerPassword=Read-Host 'Новый пароль отдельной учётной записи DSHAudit' -AsSecureString
$workerPassword=Read-Host 'Новый пароль отдельной учётной записи DSHAgent' -AsSecureString
& C:\DSH\kit\Initialize-WindowsWorker.ps1 -ConfirmAccountChanges -ControllerPassword $controllerPassword -WorkerPassword $workerPassword
& C:\DSH\kit\Freeze-WindowsPermissions.ps1 -PlanOnly
& C:\DSH\kit\Freeze-WindowsPermissions.ps1
```

Scripts создают/сбрасывают пароли DSHAudit и DSHAgent, дают контроллеру SeAssignPrimaryTokenPrivilege/SeIncreaseQuotaPrivilege и меняют ACL новой установки. Они не предназначены для существующих одноимённых accounts. Пароль worker сохраняется в защищённом `data/worker-credentials.json` для Windows runner; никогда не коммитьте этот файл. Исходники/config должны быть доступны worker только на чтение. Не запускайте installer на основном компьютере без осознанного выбора новой установки.

6. Завершите Admin-сессию, войдите в новый DSHAudit, откройте обычный PowerShell 7:

```powershell
& C:\DSH\kit\Freeze-WindowsPermissions.ps1 -Verify
Test-Path C:\DSH\source\deepseek-harness-master\apps\cli\lib\bin.js
& C:\DSH\kit\Run-Harness.ps1 -Profile web
```

`ACL_VERIFIED` и наличие bin.js подтверждают только указанные условия установки. Успешный ответ требует backend; проверку связи выполните по [запуску](RUN_WINDOWS11_RU.md). При ошибке аккаунтов/ACL не обходите её запуском Harness под Admin. Остановите процесс Ctrl+C. Для удаления установки сначала остановите Harness и вручную проверьте созданные accounts/права по сохранённым admin-evidence; автоматический uninstall здесь не заявляется.
