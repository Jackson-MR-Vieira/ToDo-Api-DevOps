from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo da tarefa
class Task(BaseModel):
    title: str

tasks = []

@app.get("/")
def home():
    return {"message": "API ToDo funcionando!"}

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    return tasks