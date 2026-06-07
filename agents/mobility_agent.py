from google.adk.agents import Agent
from schemas.mobility_schema import MobilityRecommendation

from tools.mobility_tools import (
    recommend_internal_candidates
)


mobility_agent = Agent(

    name="mobility_agent",

    model="gemini-3.5-flash",

    description="""
    Handles internal mobility
    recommendations and career
    transition analysis.
    """,

    instruction="""
    You are the Mobility Advisor.

    Your responsibilities:

    - Recommend employees
      suitable for a role

    - Analyze internal mobility

    - Suggest role transitions

    Always use the provided tool.

    Never invent employee
    recommendations.
    """,

    tools=[
        recommend_internal_candidates
    ],
    output_schema=MobilityRecommendation,
    output_key="mobility_analysis"
)