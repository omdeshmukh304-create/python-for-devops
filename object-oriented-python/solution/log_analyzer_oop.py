import json
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")
LOG_FILE = str(Path(__file__).parent.parent / "app.log")


class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.counts = {level: 0 for level in LEVELS}

    def read_logs(self):
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            print("Log file not found:", self.log_file)
            return []

    def analyze(self, lines):
        for line in lines:
            tokens = set(line.split())
            for level in LEVELS:
                if level in tokens:
                    self.counts[level] += 1
        return self.counts

    def write_summary(self, path="log_counts.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.counts, f, indent=2)


def main():
    analyzer = LogAnalyzer(LOG_FILE)
    lines = analyzer.read_logs()
    if not lines:
        print("No logs to analyze.")
        return

    result = analyzer.analyze(lines)
    for level, count in result.items():
        print(f"{level:7}: {count}")


if __name__ == "__main__":
    main()
