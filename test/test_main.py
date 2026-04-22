from src.main import *
from fastapi.testclient import TestClient

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["title"] == "Estudar Python em DevOps!"

def test_create_task():
    response = client.post("/tasks", json={"title": "Estudar Python em DevOps!"})
    assert response.status_code == 200
    assert response.json()["title"] == "Estudar Python em DevOps!"


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_multiple_tasks():
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})

    response = client.get("/tasks")
    assert len(response.json()) >= 2


def test_task_structure():
    response = client.post("/tasks", json={"title": "Nova tarefa"})
    data = response.json()

    assert "title" in data
    assert data["title"] == "Nova tarefa"