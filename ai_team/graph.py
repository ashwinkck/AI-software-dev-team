from langgraph.graph import StateGraph, START, END
from ai_team.state import AgentState
from ai_team.agents.planner import planner
from ai_team.agents.researcher import researcher
from ai_team.agents.coder import coder


def route(state: AgentState):
    return state["decision"]


graph_builder = StateGraph(AgentState)

graph_builder.add_node("planner", planner)
graph_builder.add_node("research", researcher)
graph_builder.add_node("code", coder)

graph_builder.add_edge(START, "planner")

graph_builder.add_conditional_edges(
    "planner",
    route,
    {
        "research": "research",
        "code": "code",
    },
)

graph_builder.add_edge("research", END)
graph_builder.add_edge("code", END)

graph = graph_builder.compile()