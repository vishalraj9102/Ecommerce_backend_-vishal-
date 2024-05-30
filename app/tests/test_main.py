import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_file():
    response = client.post("/upload/", files={"file": ("filename.txt", b"some content")})
    assert response.status_code == 200
    assert "file_location" in response.json()

def test_get_file():
    response = client.get("/files/filename.txt")
    assert response.status_code == 200
    assert "file_path" in response.json()
