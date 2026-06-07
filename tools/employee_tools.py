import json
from pathlib import Path

from schemas.employee_schema import EmployeeInfo


DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "employees.json"
)


def load_employees():
    """
    Load all employees from JSON file.
    """

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_employee_details_by_id(
    employee_id: str
) -> EmployeeInfo:
    """
    Retrieve employee details using employee ID.
    """

    employees = load_employees()

    for employee in employees:

        if employee["employee_id"].lower() == employee_id.lower():

            return EmployeeInfo(
                employee_id=employee["employee_id"],
                name=employee["name"],
                department=employee["department"],
                role=employee["role"],
                manager=employee["manager"],
                experience_years=employee["experience_years"]
            )

    raise ValueError(
        f"Employee '{employee_id}' not found."
    )


def get_employee_details_by_name(
    employee_name: str
) -> EmployeeInfo:
    """
    Retrieve employee details using employee name.
    """

    employees = load_employees()

    for employee in employees:

        if employee["name"].lower() == employee_name.lower():

            return EmployeeInfo(
                employee_id=employee["employee_id"],
                name=employee["name"],
                department=employee["department"],
                role=employee["role"],
                manager=employee["manager"],
                experience_years=employee["experience_years"]
            )

    raise ValueError(
        f"Employee '{employee_name}' not found."
    )


def get_employee_manager(
    employee_id: str
) -> str:
    """
    Get manager name for employee.
    """

    employee = get_employee_details_by_id(
        employee_id
    )

    return (
        employee.manager
        if employee.manager
        else "No Manager Assigned"
    )


def get_employee_department(
    employee_id: str
) -> str:
    """
    Get employee department.
    """

    employee = get_employee_details_by_id(
        employee_id
    )

    return employee.department


def get_employee_role(
    employee_id: str
) -> str:
    """
    Get employee role.
    """

    employee = get_employee_details_by_id(
        employee_id
    )

    return employee.role


def get_all_employees():
    """
    Return all employees.
    Useful for mobility and successor agents.
    """

    employees = load_employees()

    return [
        EmployeeInfo(
            employee_id=employee["employee_id"],
            name=employee["name"],
            department=employee["department"],
            role=employee["role"],
            manager=employee["manager"],
            experience_years=employee["experience_years"]
        )
        for employee in employees
    ]