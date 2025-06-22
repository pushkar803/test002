from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_upload_file():
    response = client.post("/upload/", files={"file": ("test.txt", b"file content")})
    assert response.status_code == 200
    assert response.json() == {"filename": "test.txt"}


def test_invalid_file_upload():
    response = client.post("/upload/")
    assert response.status_code == 422
