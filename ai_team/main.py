from ai_team.graph import graph

initial_state = {
    "task": "Research the best authentication methods.",
    "decision": "",
    "research": "",
    "code": "",
    "review": "",
    "documentation": "",
}

result = graph.invoke(initial_state)

print(result)   