# Your turn: finish build_agent() so the agent runs.
# Start ollama first:  ollama serve  &&  ollama pull llama3.2

import os
import sys
from pathlib import Path

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from log_utils import LEVELS, count_log_levels, read_log_file

APP_LOG = str(Path(__file__).parent.parent / "app.log")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")

SYSTEM_PROMPT = (
    "You are a Log Analysis Agent. Always use the analyze_log_file tool to get "
    "exact counts, never guess. State the counts, then a short summary."
)


@tool
def analyze_log_file(path: str) -> str:
    """Read a .log file and return the count of INFO, WARNING and ERROR lines."""
    counts = count_log_levels(read_log_file(path))
    return ", ".join(f"{level}={counts[level]}" for level in LEVELS)


def build_agent():
    # TODO: create a ChatOllama model (model=MODEL, base_url, temperature=0)
    # TODO: return create_agent(model, tools=[analyze_log_file], system_prompt=SYSTEM_PROMPT)
    raise NotImplementedError


def main():
    print("Counts:", count_log_levels(read_log_file(APP_LOG)))
    # TODO: build the agent, invoke it with a HumanMessage asking to analyze
    #       APP_LOG, then print result["messages"][-1].content


if __name__ == "__main__":
    main()
