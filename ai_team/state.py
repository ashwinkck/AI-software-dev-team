from typing import TypedDict


class AgentState(TypedDict):
    task: str
    decision: str
    research: str
    code: str
    review: str
    documentation: str
    review_status: str