# Building CLI Tools with argparse

`kubectl`, `terraform`, `aws`, `helm` — a lot of the DevOps world runs on CLIs.
This module turns the log analyzer into a real command-line tool.

Using Python's built-in [`argparse`](https://docs.python.org/3/library/argparse.html),
you'll accept a log file path, an optional output path, and an optional level
filter — with friendly error messages when inputs are wrong.

---

## Learning objectives

- Parse command-line arguments with `argparse`
- Define required (`--file`) and optional (`--out`, `--level`) arguments
- Validate input and exit with a clear message + non-zero code on error
- Reuse logic instead of rewriting it (the same counting core as the other modules)

## Setup

Pure standard library — no dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

## What's inside

```
cli-tools-argparse/
├── app.log
├── examples/
│   └── log_analyzer_cli.py     # full CLI tool
├── practice/
│   ├── log_analyzer_cli.py
│   └── README.md
└── solution/
    └── log_analyzer_cli.py
```

## How to run

```bash
# Basic: analyze a log file
python examples/log_analyzer_cli.py --file app.log

# Write the summary to a file
python examples/log_analyzer_cli.py --file app.log --out summary.json

# Filter to a single level
python examples/log_analyzer_cli.py --file app.log --level ERROR

# See the auto-generated help
python examples/log_analyzer_cli.py --help
```

Example:

```
$ python examples/log_analyzer_cli.py --file app.log
INFO   : 10
WARNING: 2
ERROR  : 3
```

If the file is missing, the tool prints a friendly error and exits with code 2:

```
$ python examples/log_analyzer_cli.py --file nope.log
Error: log file not found: nope.log
```

## Practice

See [`practice/README.md`](practice/README.md).
