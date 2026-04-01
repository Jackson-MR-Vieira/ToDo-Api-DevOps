from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_create_task():
    response = client.post("/tasks", json={"title": "Estudar DevOps"})
    assert response.status_code == 200