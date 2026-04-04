import os
import sys
import pytest

from src.main import app

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestGetColorEndpoint:
    def test_get_color_returns_200(self, client):
        response = client.get("/get-color")
        assert response.status_code == 200

    def test_get_color_returns_json(self, client):
        response = client.get("/get-color")
        assert response.is_json

    def test_get_color_response_structure(self, client):
        response = client.get("/get-color")
        data = response.get_json()
        assert "color" in data

    def test_get_color_value(self, client):
        response = client.get("/get-color")
        data = response.get_json()
        assert data["color"] == "#2ecc71"
