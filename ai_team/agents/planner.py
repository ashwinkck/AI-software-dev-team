from ai_team.state import AgentState
from ai_team.llm import llm
from ai_team.prompts.planner import PLANNER_PROMPT
from ai_team.schemas.planner import PlannerDecision

structured_llm = llm.with_structured_output(
    PlannerDecision
)

def planner(state: AgentState):
    prompt = PLANNER_PROMPT.format(
        task=state["task"]
    )

    response = structured_llm.invoke(prompt)

    return {
        "decision": response.decision
    }