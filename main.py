from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "API ToDo funcionando"}

@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    return tasks