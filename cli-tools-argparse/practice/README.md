# Practice: Log Analyzer CLI

## Your task

Complete `practice/log_analyzer_cli.py` so it works as a CLI:

1. Add a required `--file` argument.
2. Add optional `--out` (output JSON path) and `--level` (one of INFO/WARNING/ERROR).
3. If `--file` doesn't exist, print a friendly error and `sys.exit(2)`.
4. Count the levels and print the summary (or just the `--level` if given).
5. If `--out` is provided, write the counts as JSON.

## Run it

```bash
python practice/log_analyzer_cli.py --file ../app.log
python practice/log_analyzer_cli.py --help
```

## Done?

Compare with [`../solution/log_analyzer_cli.py`](../solution/log_analyzer_cli.py).
