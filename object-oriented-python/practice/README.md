# Practice: LogAnalyzer class

## Your task

Complete the `LogAnalyzer` class in `practice/log_analyzer_oop.py`:

1. In `__init__`, store the log file path and initialize a `counts` dict.
2. Implement `read_logs()` to return the file's lines (handle missing file).
3. Implement `analyze()` to count `INFO` / `WARNING` / `ERROR` — remember to
   check `LEVEL in tokens`, not `not in`.
4. Create a `LogAnalyzer` object and print the summary.
5. Bonus: add a `write_summary()` method that dumps `counts` to JSON.

Expected counts for the bundled log: `INFO=10, WARNING=2, ERROR=3`.

## Run it

```bash
python practice/log_analyzer_oop.py
```

## Done?

Compare with [`../solution/log_analyzer_oop.py`](../solution/log_analyzer_oop.py).
