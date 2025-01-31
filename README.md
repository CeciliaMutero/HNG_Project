HNG12 Stage 0 Backend Task

Public API to Retrieve Basic Information

This is a simple Django-based API that returns basic information in JSON format. It is designed for the HNG12 Stage 0 Backend Task and provides the following details:

Your registered email address (used to register on the HNG12 Slack workspace).

The current datetime in ISO 8601 UTC format.

The GitHub URL of the project's codebase.

API Endpoint

Base URL: <your-deployed-url>

GET /api/

Response Format (200 OK)

{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}

Tech Stack

Django (Python web framework)

Django REST Framework (API development)

CORS Handling (django-cors-headers)

Deployed on: <your-deployment-platform>

Getting Started

1. Clone the Repository

git clone https://github.com/yourusername/your-repo.git
cd your-repo

2. Set Up Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run Migrations

python manage.py migrate

5. Start Development Server

python manage.py runserver

Visit http://127.0.0.1:8000/api/ to see the API response.