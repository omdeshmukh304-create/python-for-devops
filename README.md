# Python for DevOps + Agentic AI

Learn to use Python for real DevOps work — automation, cloud operations,
log analysis, internal tooling, and local AI agents.

The focus is not Python syntax for its own sake, but thinking like a DevOps
engineer using Python. The course is organized into topic modules (not days),
so you can follow it live, watch it recorded, or jump straight to the topic you
need.

---

## Objective

By the end, you'll be able to say (and prove) "I use Python to solve DevOps
problems."

Each module is self-contained: it has its own README, runnable examples,
practice exercises, and worked solutions, plus any sample data it needs.

---

## Modules

Recommended learning path (each module stands alone, but this order builds
naturally):

| # | Module | You'll learn |
|---|--------|--------------|
| 1 | [python-foundations](python-foundations/) | Variables, control flow, functions, `psutil` system health |
| 2 | [apis-and-json](apis-and-json/) | `requests`, JSON, dict/list/set, file I/O, env-var secrets |
| 3 | [file-handling-and-logs](file-handling-and-logs/) | Reading files, counting log levels, writing summaries |
| 4 | [object-oriented-python](object-oriented-python/) | Practical OOP — the log analyzer as a class |
| 5 | [cli-tools-argparse](cli-tools-argparse/) | Real CLI tools with `argparse` |
| 6 | [aws-automation-boto3](aws-automation-boto3/) | Boto3 (read-only), AWS reporting, IaC intro with CDK |
| 7 | [apis-with-fastapi](apis-with-fastapi/) | Internal DevOps APIs with FastAPI + uvicorn |
| 8 | [ai-agents-for-devops](ai-agents-for-devops/) | Local AI agents: LangGraph + LangChain + Ollama |
| — | [capstone](capstone/) | Assemble it all into one interview-ready project |
| — | [guides](guides/) | Design thinking, S.T.A.R interviews, DevOps mindset |

### Standard module layout

```
<module>/
├── README.md        # objectives, setup, how to run + test
├── requirements.txt # module-local dependencies (if any)
├── examples/        # commented reference code (instructor demos)
├── practice/        # exercises with TODOs for you to complete
└── solution/        # worked answers (peek only after trying!)
```

---

## Tech stack

- Python 3.10+ (3.13 recommended)
- `psutil` — system metrics
- `requests` — HTTP / APIs
- `boto3` — AWS automation; AWS CDK for IaC
- `FastAPI` + `uvicorn` — internal APIs
- `LangGraph` + `LangChain` + `Ollama` — local AI agents
- `argparse`, `json` — CLI tooling and data (standard library)

---

## Getting started

```bash
git clone <your-fork-url>
cd python-for-devops

# create a virtual environment
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# option A: install everything for the whole course
pip install -r requirements.txt

# option B: install just one module's deps
pip install -r python-foundations/requirements.txt
```

Then open any module's `README.md` and follow along.

The AI agents module additionally needs [Ollama](https://ollama.com) running
locally with `llama3.2` pulled — see
[ai-agents-for-devops/README.md](ai-agents-for-devops/README.md).

---

## Projects included

- System Health Monitor — CPU / memory / disk checks (`python-foundations`)
- Log Analyzer — script to OOP to CLI (`file-handling-and-logs`, `object-oriented-python`, `cli-tools-argparse`)
- AWS Resource Report — read-only S3 / EC2 reporting (`aws-automation-boto3`)
- Internal DevOps Utilities API — FastAPI service exposing metrics, logs and AWS info (`apis-with-fastapi`)
- Local Log Analysis Agent — LangGraph + Ollama AI agent (`ai-agents-for-devops`)
- Capstone — one clean end-to-end flow tying it together (`capstone`)

---

## Who this is for

- Beginners in Python
- DevOps, SRE, Cloud, and Automation engineers
- Freshers and career switchers adding Python automation skills

---

## How to use this repository

1. Fork the repo; sync your fork to get updates.
2. Create and activate a virtual environment.
3. Install dependencies (whole course or per-module).
4. Work through modules in order, or jump to the topic you need.
5. Do the `practice/` exercises before peeking at `solution/`.
6. Push your work and share your progress.

---

Happy Learning

**TrainWithShubham**
