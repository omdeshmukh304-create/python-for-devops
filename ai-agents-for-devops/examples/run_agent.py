# Log analysis agent using langchain + a local Ollama model.
# Start ollama first:  ollama serve  &&  ollama pull llama3.2
#   python run_agent.py
#   OLLAMA_MODEL=qwen3-coder:30b python run_agent.py

import os
from pathlib import Path

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from log_utils import LEVELS, count_log_levels, read_log_file

APP_LOG = str(Path(__file__).parent.parent / "app.log")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")

SYSTEM_PROMPT = (
    "You are a Log Analysis Agent for DevOps engineers. "
    "Always use the analyze_log_file tool to get exact counts, never guess. "
    "State the INFO/WARNING/ERROR counts, then give a one or two line summary. "
    "Suggest ideas only, never perform production actions."
)


@tool
def analyze_log_file(path: str) -> str:
    """Read a .log file and return the count of INFO, WARNING and ERROR lines."""
    counts = count_log_levels(read_log_file(path))
    return ", ".join(f"{level}={counts[level]}" for level in LEVELS)


def build_agent():
    model = ChatOllama(model=MODEL, base_url="http://localhost:11434", temperature=0)
    return create_agent(model, tools=[analyze_log_file], system_prompt=SYSTEM_PROMPT)


def main():
    # The counts come from the tool, not the model, so they're always right.
    print(f"Model: {MODEL}")
    print("Counts:", count_log_levels(read_log_file(APP_LOG)))

    agent = build_agent()
    result = agent.invoke(
        {"messages": [HumanMessage(content=f"Analyze the log file at {APP_LOG}.")]},
        {"recursion_limit": 10},
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
