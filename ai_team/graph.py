from langgraph.graph import StateGraph, START, END

from ai_team.state import AgentState
from ai_team.agents.planner import planner


graph_builder = StateGraph(AgentState)

graph_builder.add_node("planner", planner)

graph_builder.add_edge(START, "planner")

graph_builder.add_edge("planner", END)

graph = graph_builder.compile()