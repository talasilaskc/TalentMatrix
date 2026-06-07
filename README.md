# TalentMatrix

TalentMatrix is an employee agentic helper system built using the Google Agent Development Kit (ADK). It features multiple specialized agents communicating via a shared session state to assist with employee information lookup, leave balance management, internal mobility transitions, and more.

## Setup Instructions

If setting up this project from scratch, follow these steps:

### 1. Clone the repository
```powershell
git clone https://github.com/talasilaskc/TalentMatrix.git
cd TalentMatrix
```

### 2. Create a virtual environment
```powershell
python -m venv venv
```

### 3. Activate the virtual environment
* **On Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
* **On Windows (Command Prompt - CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
* **On macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install dependencies
```powershell
pip install -r requirements.txt
```

### 5. Set up your environment variables
Create a `.env` file in the root directory and add your Google AI Gemini API Key:
```env
GOOGLE_API_KEY="your-gemini-api-key-here"
```

### 6. Start the ADK Developer Web UI
```powershell
adk web .
```

---

## Current Agent Directory

* **Employee Information Agent**: Handles profile retrieval, manager lookup, department, and role checks.
* **Leave Management Agent**: Queries leave balances, used leaves, and pending requests.
* **Mobility Advisor**: Identifies role transition opportunities and rates suitability based on skill matches.
* **Coordinator Agent**: Receives and automatically routes user requests to the appropriate specialist agent.
