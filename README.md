# Task Manager REST API (Django)

![Django REST Framework](https://img.shields.io/badge/Django-REST%20Framework-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)

A simple yet powerful RESTful API for task management built with Django and Django REST Framework.

## Features

- ✅ Create, read, update, and delete tasks
- ✅ Mark tasks as completed
- ✅ Lightweight SQLite database (default)
- ✅ Clean RESTful endpoints
- ✅ Optional status page with HTML/CSS

## API Endpoints

| Method | Endpoint          | Description                     |
|--------|-------------------|---------------------------------|
| GET    | /api/tasks/     | Retrieve all tasks              |
| POST   | /api/tasks/     | Create a new task               |
| PUT    | /api/tasks/<id> | Update a task (mark completed)  |
| DELETE | /api/tasks/<id> | Delete a task                   |

## Request/Response Examples

Create a Task (POST /api/tasks/)
{
    "title": "What's uppp"
}
Response
{
    "id": 1,
    "title": "Buy groceries",
    "completed": false,
    "created_at": "2023-10-25T12:00:00Z",
    "updated_at": "2023-10-25T12:00:00Z"
}
## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
  
   git clone https://github.com/yourusername/taskmanager.git
   cd taskmanager
   
2. Create and activate a virtual environment:
  
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
    
3. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate
   
### Running the Server

python manage.py runserver
The API will be available at http://localhost:8000/

## Testing the API

You can test the API usingc Postman:

# Get all tasks
curl http://localhost:8000/api/tasks/

# Create a task
curl -X POST -H "Content-Type: application/json" -d '{"title":"New Task"}' http://localhost:8000/api/tasks/

# Update a task (mark as completed)
curl -X PUT -H "Content-Type: application/json" -d '{"completed":true}' http://localhost:8000/api/tasks/1/

# Delete a task
curl -X DELETE http://localhost:8000/api/tasks/1/
## Database Configuration

By default, the project uses SQLite.
Filtering Capabilites
  you can filter tasks by their completions status 
## Project Structure

taskmanager/
├── db.sqlite3                # SQLite database (dev)
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── taskmanager/              # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Database and app config
│   ├── urls.py               # URL routing
│   └── wsgi.py
└── tasks/                    # Tasks app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/           # Database migrations
    ├── models.py             # Task model
    ├── serializers.py        # API serializers
    ├── templates/            # HTML templates
    ├── tests.py
    └── views.py              # API views
