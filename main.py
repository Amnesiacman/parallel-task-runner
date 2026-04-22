#!/usr/bin/env python3
import argparse
import json


def build_parser():
    p = argparse.ArgumentParser(prog="parallel-task-runner")
    p.add_argument("--format", choices=["text", "json"], default="text")
    p.add_argument("--dry-run", action="store_true")
    return p


def main():
    args = build_parser().parse_args()
    payload = {"project": "parallel-task-runner", "status": "ok", "dry_run": args.dry_run}
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=True))
    else:
        print(f"[{payload['project']}] status={payload['status']} dry_run={payload['dry_run']}")


if __name__ == "__main__":
    main()
