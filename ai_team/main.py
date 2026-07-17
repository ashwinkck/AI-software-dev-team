from ai_team.graph import graph

initial_state = {
    "task": "Build a weather API",
    "decision": "",
    "research": "",
    "code": "",
    "review": "",
    "documentation": "",
}
result = graph.invoke(initial_state)