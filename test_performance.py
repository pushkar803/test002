from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_performance_large_file():
    with open("test_large.pdf", "rb") as file:
        response = client.post(
            "/upload/", files={"file": ("test_large.pdf", file, "application/pdf")}
        )
        assert response.status_code == 201
