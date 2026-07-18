from typing import Literal
from pydantic import BaseModel

class PlannerDecision(BaseModel):

    decision: Literal["research", "code"]