from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_unauthorized_access():
    response = client.post(
        "/upload/", files={"file": ("test.pdf", b"dummy content", "application/pdf")}
    )
    assert response.status_code == 401
