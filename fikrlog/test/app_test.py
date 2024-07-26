import pytest 
from app import app as flask_app

@pytest.fixture
def app():
    return flask_app


def test_get_articles(client):
    response = client.get('/blog/no-article')
    assert response.status_code == 404