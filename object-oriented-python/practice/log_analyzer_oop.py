# Practice: build the LogAnalyzer class.

from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")
LOG_FILE = str(Path(__file__).parent.parent / "app.log")


class LogAnalyzer:
    def __init__(self, log_file):
        # TODO 1: store log_file and initialize self.counts
        raise NotImplementedError("Implement __init__")

    def read_logs(self):
        # TODO 2: open self.log_file, return its lines (handle FileNotFoundError)
        raise NotImplementedError("Implement read_logs")

    def analyze(self, lines):
        # TODO 3: count INFO / WARNING / ERROR using `LEVEL in tokens`
        raise NotImplementedError("Implement analyze")


def main():
    analyzer = LogAnalyzer(LOG_FILE)
    lines = analyzer.read_logs()
    print(analyzer.analyze(lines))


if __name__ == "__main__":
    main()
