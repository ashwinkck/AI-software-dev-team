from ai_team.state import AgentState
from ai_team.llm import llm
from ai_team.prompts.planner import PLANNER_PROMPT

def planner(state: AgentState):
    prompt = PLANNER_PROMPT.format(
        task=state["task"]
    )

    response = llm.invoke(prompt)

    decision = response.content.strip().lower()

    if decision not in {"research", "code"}:
        decision = "research"

    return {
        "decision": decision
    }