from schemas.employee_schema import EmployeeInfo
from google.adk.agents import Agent

from tools.employee_tools import (
    get_employee_details_by_id,
    get_employee_details_by_name,
    get_employee_manager,
    get_employee_department,
    get_employee_role
)

employee_agent= Agent(
    name="employee_agent",
    model="gemini-3.5-flash",
     description=(
        "Handles employee information retrieval."
    ),

    instruction="""
    You are an Employee Information Agent.

    Your responsibilities:

    - Retrieve employee details
    - Retrieve employee manager
    - Retrieve employee department
    - Retrieve employee role

    Use the available tools whenever
    employee information is requested.

    Always use tools rather than
    making assumptions.
    """,
    tools=[
        get_employee_details_by_id,
        get_employee_details_by_name,
        get_employee_manager,
        get_employee_department,
        get_employee_role
    ],
    output_schema=EmployeeInfo,
    output_key="employee_info"
)

