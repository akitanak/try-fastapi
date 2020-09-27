from fastapi.testclient import TestClient
from try_fastapi.api import app

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "I'm Healthy!"}
