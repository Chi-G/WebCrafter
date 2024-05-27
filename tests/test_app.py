import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to WebCrafter" in response.data
