from pydantic import BaseModel


class LeaveInfo(BaseModel):
    employee_id: str
    remaining_leaves: int
    used_leaves: int
    pending_requests: int