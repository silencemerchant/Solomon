#!/usr/bin/env python3
"""Simple self-improve scaffold.

This script applies a small, safe set of automated fixes discovered previously:
- Fix import path in core/orchestrator.py
- Fix stray characters in app/main.py
- Ensure package __init__.py files exist for solomon, solomon/core, solomon/core/agents

It writes a summary (JSON) to stdout or to --output file and exits 0.
It does not push or open PRs; the workflow action will create a PR from workspace changes.
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FIXES = []


def replace_in_file(path: Path, old: str, new: str):
    text = path.read_text()
    if old in text:
        new_text = text.replace(old, new)
        path.write_text(new_text)
        return True
    return False


def ensure_init(path: Path):
    if not path.exists():
        path.write_text('# Package init for {}\n'.format(path))
        return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=None)
    args = parser.parse_args()

    changes = []

    # Fix import path in core/orchestrator.py
    orchestrator = ROOT / 'core' / 'orchestrator.py'
    if orchestrator.exists():
        old = 'from solomon.agents.counter_surv_agent import CounterSurvAgent'
        new = 'from solomon.core.agents.counter_surv_agent import CounterSurvAgent'
        if replace_in_file(orchestrator, old, new):
            changes.append({'file': str(orchestrator.relative_to(ROOT)), 'change': 'fixed import path'})

    # Fix stray character in app/main.py
    app_main = ROOT / 'app' / 'main.py'
    if app_main.exists():
        text = app_main.read_text()
        if text.endswith('\n'):
            pass
        # Remove stray 'q' occurring at end of health return (very targeted)
        if 'return {"status": "healthy", "version": "0.1"}q' in text:
            new_text = text.replace('return {"status": "healthy", "version": "0.1"}q', 'return {"status": "healthy", "version": "0.1"}')
            app_main.write_text(new_text)
            changes.append({'file': str(app_main.relative_to(ROOT)), 'change': 'removed stray q in return'})

    # Ensure __init__.py files exist in package dirs
    pkg_paths = [ROOT / 'solomon', ROOT / 'solomon' / 'core', ROOT / 'solomon' / 'core' / 'agents']
    for p in pkg_paths:
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
        init = p / '__init__.py'
        if ensure_init(init):
            changes.append({'file': str(init.relative_to(ROOT)), 'change': 'added __init__'})

    # Summary
    summary = {'changes': changes}

    out = json.dumps(summary, indent=2)
    if args.output:
        Path(args.output).write_text(out)
    else:
        print(out)

    # Exit normally - create-pull-request action will pick up staged changes in workspace

if __name__ == '__main__':
    main()
