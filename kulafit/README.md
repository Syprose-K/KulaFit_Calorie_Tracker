# KulaFit Calorie Tracker

KulaFit is a Kenyan-focused calorie tracker that helps users monitor their daily food intake, track calories, and manage macronutrients using locally available Kenyan foods.

## Features

- **User Accounts**: Register, log in, and manage your profile.
- **Food Database**: CRUD operations for foods (admin).
- **Meal Logging**: Track meals and calorie intake.
- **Weight Logging**: Record weight progress over time.
- **Dashboard**: See calorie and macronutrient summaries.
- **Kenyan Food Focus**: Includes local foods and serving sizes.

## Technology Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL / SQLite (for development)
- **API**: REST API endpoints for foods, meals, and weights

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Syprose-K/KulaFit_Calorie_Tracker.git
cd kulafit

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Apply migrations:
    python manage.py migrate

5. Run the development server:
    python manage.py runserver

API Endpoints

Foods: /api/foods/
Meal Logs: /api/meals/
Weight Logs: /api/weights/
Dashboard: /api/dashboard/

Contributing

Fork the repo
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add feature')
Push to branch (git push origin feature/your-feature)
Open a Pull Request

License
This project is licensed under the MIT License.