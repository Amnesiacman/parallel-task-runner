import json
from pathlib import Path

from parallel_task_runner.cli import main


def test_cli_json(tmp_path: Path, capsys):
    commands = tmp_path / "commands.txt"
    commands.write_text("echo one\necho two\n", encoding="utf-8")
    code = main(["--commands-file", str(commands), "--format", "json"])
    payload = json.loads(capsys.readouterr().out.strip())
    assert code == 0
    assert payload["total"] == 2


def test_cli_strict_fails(tmp_path: Path):
    commands = tmp_path / "commands.txt"
    commands.write_text("python3 -c 'import sys; sys.exit(1)'\n", encoding="utf-8")
    code = main(["--commands-file", str(commands), "--strict"])
    assert code == 1

