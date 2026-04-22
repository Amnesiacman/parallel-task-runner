import argparse
import json
from pathlib import Path

from parallel_task_runner.runner import run_parallel


def _read_commands(path: Path) -> list[str]:
    commands = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        commands.append(line)
    return commands


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="parallel-task-runner",
        description="Run commands in parallel and produce structured report",
    )
    parser.add_argument("--commands-file", required=True, help="Path to text file with commands")
    parser.add_argument("--cwd", default=".", help="Working directory for commands")
    parser.add_argument("--max-workers", type=int, default=2, help="Parallel workers limit")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--strict", action="store_true", help="Return code 1 if any command fails")
    return parser


def _render_text(report: dict) -> str:
    lines = [
        f"CWD: {report['cwd']}",
        f"Total: {report['total']}",
        f"Failed: {report['failed']}",
        f"Status: {'ok' if report['ok'] else 'failed'}",
        "",
    ]
    for item in report["results"]:
        marker = "OK" if item["return_code"] == 0 else "FAIL"
        lines.append(f"- [{marker}] {item['command']}")
        if item["stderr"]:
            lines.append(f"  stderr: {item['stderr']}")
    return "\n".join(lines).rstrip()


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    commands = _read_commands(Path(args.commands_file))
    report = run_parallel(commands, cwd=Path(args.cwd), max_workers=args.max_workers)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=True))
    else:
        print(_render_text(report))
    if args.strict and not report["ok"]:
        return 1
    return 0

