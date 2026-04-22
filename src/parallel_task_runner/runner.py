import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path


@dataclass
class TaskResult:
    command: str
    return_code: int
    stdout: str
    stderr: str


def _run_one(command: str, cwd: Path) -> TaskResult:
    proc = subprocess.run(
        command,
        cwd=str(cwd),
        shell=True,
        text=True,
        capture_output=True,
    )
    return TaskResult(
        command=command,
        return_code=proc.returncode,
        stdout=proc.stdout,
        stderr=proc.stderr,
    )


def run_parallel(commands: list[str], cwd: Path, max_workers: int = 2) -> dict:
    results: list[TaskResult] = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(_run_one, cmd, cwd) for cmd in commands]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda x: commands.index(x.command))
    failed = [r for r in results if r.return_code != 0]
    return {
        "cwd": str(cwd),
        "total": len(results),
        "failed": len(failed),
        "ok": len(failed) == 0,
        "results": [
            {
                "command": r.command,
                "return_code": r.return_code,
                "stdout": r.stdout.strip(),
                "stderr": r.stderr.strip(),
            }
            for r in results
        ],
    }
