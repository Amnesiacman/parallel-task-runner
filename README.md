# parallel-task-runner

`parallel-task-runner` выполняет список shell-команд параллельно и строит единый отчёт.

## Что умеет v0.1

- читает команды из файла (`--commands-file`)
- ограничивает параллелизм (`--max-workers`)
- выводит отчёт в `text` или `json`
- в `--strict` режиме возвращает код `1`, если хоть одна команда упала

## Использование

```bash
python3 -m pip install -e .
parallel-task-runner --commands-file ./commands.txt --max-workers 3 --format json
```

Пример `commands.txt`:

```text
echo lint
echo test
python3 -c "print('ok')"
```
