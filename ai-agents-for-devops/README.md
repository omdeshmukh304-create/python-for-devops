# AI Agents for DevOps (LangGraph + LangChain + Ollama)

Build a local, private AI agent that reads log files and explains what happened,
running entirely on your machine with [Ollama](https://ollama.com), orchestrated
with [LangGraph](https://langchain-ai.github.io/langgraph/) and
[LangChain](https://python.langchain.com/).

The design principle that keeps this reliable: the tool does the math, the LLM
writes the story.

A plain, deterministic Python function counts the log levels (and is unit-tested
without any LLM). The agent's job is only to *call that tool* and summarize the
result in plain English — so the numbers are always correct even if a small
local model is imperfect at tool-calling.

---

## Learning objectives

- Understand what an agent is: an LLM that can decide to call tools
- Wrap a Python function as a LangChain `@tool`
- Run a local LLM with `ChatOllama` (no API keys, no cloud)
- Build an agent with LangChain's `create_agent` (the modern 1.0 API)
- See what that agent does under the hood with a custom LangGraph `StateGraph`
- Keep deterministic logic testable and separate from the LLM

---

## Prerequisites

1. Ollama installed and running:
   ```bash
   # install from https://ollama.com, then:
   ollama serve                 # starts the server on http://localhost:11434
   ollama pull llama3.2         # default model (small, ~2GB)
   ```
   Verify it's up and the model is present:
   ```bash
   curl http://localhost:11434/api/tags     # should list llama3.2
   ```

   Model choice: the default is `llama3.2` because it's small and runs
   anywhere. It reliably calls the tool, but its written summary can be generic.
   For sharper summaries, use a stronger tool-calling model and set the
   `OLLAMA_MODEL` env var:
   ```bash
   ollama pull qwen3-coder:30b
   OLLAMA_MODEL=qwen3-coder:30b python examples/run_agent.py
   ```

2. Python environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## What's inside

```
ai-agents-for-devops/
├── app.log                     # sample log to analyze
├── requirements.txt
├── examples/
│   ├── log_utils.py            # deterministic counting core (NO LLM)
│   └── run_agent.py            # the agent, via create_agent
├── practice/
│   ├── run_agent.py            # your turn — wire up the agent
│   └── README.md
└── solution/
    ├── log_utils.py
    ├── run_agent.py            # create_agent + custom StateGraph variant
    └── test_log_utils.py       # pytest — runs with NO Ollama needed
```

## How to run

```bash
# Deterministic tests — no Ollama required, always pass
python -m pytest solution -v

# The agent demo — needs Ollama running with llama3.2
python examples/run_agent.py
```

Expected: the agent reports something like
`INFO=10, WARNING=2, ERROR=3` plus a short root-cause-style summary. The demo
also prints the deterministic counts directly as a fallback, so you always see
correct numbers.

---

## Two ways to build the agent

- `create_agent` (in `examples/`) — the batteries-included way from LangChain
  1.0. One line gives you the agent-to-tools reasoning loop.
- Custom `StateGraph` (in `solution/run_agent.py custom`) — the same loop built
  by hand with LangGraph: a state with a message reducer, an `agent` node, a
  `ToolNode`, and a conditional edge. This is how you see what `create_agent`
  does for you.

Note: earlier LangGraph used `create_react_agent`; in LangGraph/LangChain 1.0
the stable API is `create_agent` from `langchain.agents`. This module uses the
current one.

## Gotchas with small local models

Small models like `llama3.2` sometimes skip tools or hallucinate numbers. We
keep the demo robust by:

- Setting `temperature=0` for reproducibility.
- Exposing exactly one clearly-named tool (`analyze_log_file`).
- A system prompt that says: always call the tool, never guess numbers.
- Setting a `recursion_limit` so a stuck model errors out instead of hanging.
- Printing the deterministic counts alongside the agent's answer.

## Practice

See [`practice/README.md`](practice/README.md).
