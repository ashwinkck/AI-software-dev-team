from ai_team.state import AgentState


def planner(state: AgentState):

    print("Planner Agent Executed")

    task = state["task"].lower()

    if "research" in task:
        return {
            "decision":"research"
        }
    return {
        "decision":"code"
    }