# parallel-task-runner

[English version](README.md)

Параллельный запуск shell-команд с единым отчётом.

## Возможности

- чтение команд из файла
- ограничение воркеров (`--max-workers`)
- вывод в `text`/`json`
- strict-режим для CI (`--strict`)

## Использование

```bash
python3 main.py --commands-file ./commands.txt --max-workers 3
python3 main.py --commands-file ./commands.txt --format json
python3 main.py --commands-file ./commands.txt --strict
```

Пример `commands.txt`:

```text
echo lint
echo test
python3 -c "print('ok')"
```
