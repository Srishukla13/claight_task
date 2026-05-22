# FastAPI Example Project
This project is a simple REST API built using FastAPI.

## Install Dependencies
pip install -r requirements.txt

## Run the Project
uvicorn main:app --reload

## API Endpoints
POST /tasks
GET /tasks
GET /tasks/{task_id}
PUT /tasks/{task_id}
DELETE /tasks/{task_id}

## Swagger API docs link
http://127.0.0.1:8000/docs
