import json
from pathlib import Path

from schemas.leave_schema import LeaveInfo
from tools.employee_tools import get_employee_details_by_name


DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "leave_balance.json"
)


def load_leave_data():

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def get_leave_balance(
    employee_id: str
) -> LeaveInfo:

    leave_data = load_leave_data()

    for employee in leave_data:

        if (
            employee["employee_id"].lower()
            ==
            employee_id.lower()
        ):

            return LeaveInfo(
                employee_id=employee["employee_id"],
                remaining_leaves=employee["remaining_leaves"],
                used_leaves=employee["used_leaves"],
                pending_requests=employee["pending_requests"]
            )

    raise ValueError(
        f"Employee '{employee_id}' not found."
    )


def get_leave_balance_by_name(
    employee_name: str
) -> LeaveInfo:

    employee = get_employee_details_by_name(
        employee_name
    )

    return get_leave_balance(
        employee.employee_id
    )