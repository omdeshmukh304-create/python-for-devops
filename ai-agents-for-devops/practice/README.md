# Practice: Build the Log Analysis Agent

Requires Ollama running with `llama3.2` pulled. See the module README.

## Your task

Complete `practice/run_agent.py`:

1. Create a `ChatOllama` model (`model="llama3.2"`, `base_url="http://localhost:11434"`, `temperature=0`).
2. The `analyze_log_file` tool is already written for you — pass it to the agent.
3. Build the agent with `create_agent(model, tools=[...], system_prompt=SYSTEM_PROMPT)`.
4. Invoke it with a `HumanMessage` asking it to analyze `../app.log`.
5. Print the final message.

## Verify

```bash
# First, the deterministic core (no Ollama needed):
python -m pytest ../solution -v

# Then the agent (needs Ollama):
python practice/run_agent.py
```

## Stretch goals

- Add a second tool (e.g. `tail_log` that returns the last N lines) and see how
  the agent chooses between tools.
- Rebuild the agent as a custom `StateGraph` (see `../solution/run_agent.py custom`).

## Done?

Compare with [`../solution/run_agent.py`](../solution/run_agent.py).
