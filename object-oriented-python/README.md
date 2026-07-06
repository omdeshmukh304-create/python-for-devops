# Object-Oriented Python for DevOps

Automation scripts grow into tools, and tools need structure. This module
refactors the log analyzer into a class — the way a lot of internal DevOps
tools are built.

Same behavior as [file-handling-and-logs](../file-handling-and-logs), now
organized with a class: state lives in `__init__`, and behavior lives in
methods. Light, practical OOP — no inheritance or abstract classes.

---

## Learning objectives

- Define a `class` and create objects (instances) from it
- Initialize state in `__init__()`
- Group behavior into instance methods (`read_logs`, `analyze`, `write_summary`)
- Understand *why* OOP helps: state + behavior travel together, and one object
  can be reused for multiple files

## Setup

Pure standard library — no dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

## What's inside

```
object-oriented-python/
├── app.log
├── examples/
│   └── log_analyzer_oop.py     # LogAnalyzer class + demo
├── practice/
│   ├── log_analyzer_oop.py
│   └── README.md
└── solution/
    └── log_analyzer_oop.py
```

## How to run

```bash
python examples/log_analyzer_oop.py
```

Expected: `INFO=10, WARNING=2, ERROR=3` for the bundled log.

## Practice

See [`practice/README.md`](practice/README.md).
