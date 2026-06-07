import sys
from pathlib import Path

# Add the parent directory (project root) to python path
sys.path.append(str(Path(__file__).parent.parent))

from tools.employee_tools import *

print(
    get_employee_details_by_id("E001")
)

print(
    get_employee_details_by_name("John Doe")
)

print(
    get_employee_manager("E001")
)

print(
    get_employee_department("E001")
)

print(
    get_employee_role("E001")
)
