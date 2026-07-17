from ai_team.state import AgentState
from ai_team.llm import llm

def planner(state: AgentState):

    task = state["task"]

    prompt = f"""
You are a project planner.planner

Decide whether the following task requires:

research
or
code 

Reply with only one word. 

Task:
{task}
"""
    
    response = llm.invoke(prompt)

    decision = response.content.strip().lower()

    return {
        "decision":decision
    }

