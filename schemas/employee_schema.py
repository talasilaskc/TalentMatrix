from pydantic import BaseModel


class EmployeeInfo(BaseModel):
    employee_id: str
    name: str
    department: str
    role: str
    manager: str | None = None
    experience_years: int