import json
from pathlib import Path

from schemas.mobility_schema import (
    CandidateRecommendation,
    MobilityRecommendation
)


EMPLOYEE_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "employees.json"
)

SKILLS_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "employee_skills.json"
)

ROLES_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "career_roles.json"
)


def load_json(file_path):
    """
    Load JSON data from file.
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def recommend_internal_candidates(
    target_role: str
) -> MobilityRecommendation:
    """
    Recommend employees suitable
    for a target role based on
    skill matching.
    """

    employees = load_json(
        EMPLOYEE_FILE
    )

    employee_skills = load_json(
        SKILLS_FILE
    )

    career_roles = load_json(
        ROLES_FILE
    )

    role_data = None

    for role in career_roles:

        if (
            role["target_role"].lower()
            ==
            target_role.lower()
        ):

            role_data = role
            break

    if role_data is None:

        raise ValueError(
            f"Role '{target_role}' not found."
        )

    required_skills = set(
        role_data["required_skills"]
    )

    recommendations = []

    for skill_record in employee_skills:

        employee_id = skill_record[
            "employee_id"
        ]

        employee_skill_set = set(
            skill_record["skills"]
        )

        matched_skills = (
            required_skills
            &
            employee_skill_set
        )

        fit_score = round(
            (
                len(matched_skills)
                /
                len(required_skills)
            )
            * 100,
            2
        )

        employee_name = next(
            (
                employee["name"]
                for employee in employees
                if employee["employee_id"]
                == employee_id
            ),
            "Unknown"
        )

        recommendations.append(
            CandidateRecommendation(
                employee_id=employee_id,
                employee_name=employee_name,
                fit_score=fit_score
            )
        )

    recommendations.sort(
        key=lambda candidate: candidate.fit_score,
        reverse=True
    )

    return MobilityRecommendation(
        target_role=target_role,
        recommendations=recommendations[:5]
    )