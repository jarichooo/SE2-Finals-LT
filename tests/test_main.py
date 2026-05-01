import pytest
from app.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Hello" in res.data


def test_add(client):
    res = client.get('/add/3/4')
    assert res.data == b"7"
