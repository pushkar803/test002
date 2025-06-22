from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_upload_document():
    response = client.post(
        "/upload/", files={"file": ("test.pdf", b"dummy content", "application/pdf")}
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Document uploaded successfully"}


def test_invalid_file_type():
    response = client.post(
        "/upload/", files={"file": ("test.txt", b"dummy content", "text/plain")}
    )
    assert response.status_code == 400
