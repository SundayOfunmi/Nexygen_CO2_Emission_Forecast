# Automated Tests
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

TOKEN = "mysecrettoken"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_forecast():
    response = client.get(
        "/forecast?scope=SCOPE 1",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    assert response.status_code == 200

