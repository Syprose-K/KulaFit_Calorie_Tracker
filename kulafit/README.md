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

## API Documentation

All API endpoints are prefixed with `/api/`.
Authentication is required unless stated otherwise.

---

### 🥗 Foods (Admin Only)

#### Create Food
**POST** `/api/foods/`

Request Body:
```json
{
  "name": "Ugali",
  "food_type": "starch",
  "calories_per_unit": 180,
  "protein_per_unit": 4,
  "carbs_per_unit": 38,
  "fats_per_unit": 1,
  "measurement_unit": "cup"
}

Response:
{
  "message": "Food created",
  "id": 1
}

Status Codes:
201 Created
403 Forbidden (non-admin)

🍽 Meals
Create Meal

POST /api/meals/

Request Body:
{
  "food_id": 1,
  "quantity": 2,
  "meal_type": "lunch"
}

Response:

{
  "message": "Meal created",
  "id": 10
}

Status Codes:

201 Created
400 Bad Request
401 Unauthorized

List Meals

GET /api/meals/

Response:
[
  {
    "id": 10,
    "food": "Ugali",
    "quantity": 2,
    "meal_type": "lunch",
    "calories": 360,
    "date": "2025-01-05"
  }
]

Status Codes:

200 OK
401 Unauthorized

Update Meal

PUT /api/meals/{id}/

Request Body:

{
  "quantity": 3
}

Response:
{
  "message": "Meal updated"
}

Status Codes:
200 OK
403 Forbidden
404 Not Found

Delete Meal

DELETE /api/meals/{id}/

Response:
{
  "message": "Meal deleted"
}

Status Codes:

204 No Content
403 Forbidden
404 Not Found

⚖️ Weight Logs
Log Weight

POST /api/weights/

Request Body:

{
  "weight": 72.5
}

Response:
{
  "message": "Weight logged",
  "id": 5
}

Status Codes:

201 Created
400 Bad Request
401 Unauthorized

List Weight Logs
GET /api/weights/

Response:

[
  {
    "weight": 72.5,
    "date": "2025-01-05"
  }
]
Status Codes:
200 OK
401 Unauthorized


Contributing

Fork the repo
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add feature')
Push to branch (git push origin feature/your-feature)
Open a Pull Request


## HTTP Status Codes

- 200 OK – Successful GET requests
- 201 Created – Resource created successfully
- 400 Bad Request – Invalid input or missing fields
- 401 Unauthorized – Authentication required
- 403 Forbidden – Access denied to resource
- 404 Not Found – Resource does not exist
- 500 Internal Server Error – Unexpected server errors (logged)

License
This project is licensed under the MIT License.