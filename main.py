"""
main.py - FastAPI application for task management.
This module provides REST API endpoints for creating, reading, updating, and deleting tasks.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="Task Manager API")

class Task(BaseModel):
  id:int
  title: str= Field(..., min_length=1)
  description: str= Field(..., min_length=1)
  completed: bool= False

# In-memory storage for tasks
tasks:List[Task]= []
task_id_counter= 1

def get_task(task_id: int)-> Optional[Task]:
  for task in tasks:
    if task.id== task_id:
      return task
  return None
  
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
  global task_id_counter
  # Validate title and description
  if not task.title.strip() or not task.description.strip():
    raise HTTPException(status_code=400, detail="Title and description cannot be empty.")
  task.id= task_id_counter
  tasks.append(task)
  task_id_counter+= 1
  return task

@app.get("/tasks", response_model=List[Task])
def read_tasks():
  return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
  task= get_task(task_id)
  if not task:
    raise HTTPException(status_code=404, detail="Task not found.")
  return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
  task= get_task(task_id)
  if not task:
    raise HTTPException(status_code=404, detail="Task not found.")
  if not updated_task.title.strip() or not updated_task.description.strip():
    raise HTTPException(status_code=400, detail="Title and description cannot be empty.")
  task.title = updated_task.title
  task.description = updated_task.description
  task.completed= updated_task.completed
  return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
  global tasks
  task= get_task(task_id)
  if not task:
    raise HTTPException(status_code=404, detail="Task not found.")
  tasks= [t for t in tasks if t.id != task_id]
  return {"detail": "Task deleted successfully."}
