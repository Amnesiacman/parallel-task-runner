# parallel-task-runner

[Русская версия](README.ru.md)

Run shell commands in parallel and collect deterministic reports.

## Features

- commands from file
- worker limit (`--max-workers`)
- `text`/`json` output
- strict mode for CI (`--strict`)

## Usage

```bash
python3 main.py --commands-file ./commands.txt --max-workers 3
python3 main.py --commands-file ./commands.txt --format json
python3 main.py --commands-file ./commands.txt --strict
```

Example `commands.txt`:

```text
echo lint
echo test
python3 -c "print('ok')"
```
