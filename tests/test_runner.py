from pathlib import Path

from parallel_task_runner.runner import run_parallel


def test_run_parallel_success(tmp_path: Path):
    report = run_parallel(["echo hello", "echo world"], cwd=tmp_path, max_workers=2)
    assert report["ok"] is True
    assert report["failed"] == 0
    assert report["total"] == 2


def test_run_parallel_failure(tmp_path: Path):
    report = run_parallel(["python3 -c 'import sys; sys.exit(1)'"], cwd=tmp_path, max_workers=1)
    assert report["ok"] is False
    assert report["failed"] == 1

