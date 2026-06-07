from google.adk.agents import Agent
from schemas.leave_schema import LeaveInfo

from tools.leave_tools import (
    get_leave_balance
)


leave_agent = Agent(

    name="leave_agent",

    model="gemini-3.5-flash",

    description="Handles employee leave information.",

    instruction="""
    You are a Leave Management Agent.

    Your responsibilities:

    - Retrieve employee leave balance
    - Retrieve used leaves
    - Retrieve pending leave requests

    Always use the available tool.

    Never make assumptions about
    leave information.

    If an employee ID is provided,
    use the tool to fetch leave data.

    Use the tool output to answer
    the user's question.
    """,

    tools=[
        get_leave_balance
    ],
    output_schema=LeaveInfo,
    output_key="leave_info"
)