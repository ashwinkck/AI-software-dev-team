from ai_team.state import AgentState
from ai_team.llm import llm


def planner(state: AgentState):

    task = state["task"]

    prompt = f"""
You are an AI project planner.

Your job is to classify the user's task into exactly one of these categories:

- research
- code

Rules:
- Reply with ONLY one word.
- Do not explain your answer.
- Do not include punctuation.

Task:
{task}
"""

    response = llm.invoke(prompt)

    decision = response.content.strip().lower()

    if decision not in {"research", "code"}:
        decision = "research"

    return {
        "decision": decision
    }