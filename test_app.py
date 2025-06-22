from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_upload_file():
    """
    Test for the upload_file endpoint.
    """
    response = client.post("/upload/", files={"file": ("test.txt", "file content")})
    assert response.status_code == 200
    assert response.json() == {"filename": "test.txt"}
