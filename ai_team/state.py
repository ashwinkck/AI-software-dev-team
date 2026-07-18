from typing import TypedDict

class AgentState(TypedDict):
    task: str
    decision: str
    confidence: float
    research: str
    code: str
    review: str
    documentation: str