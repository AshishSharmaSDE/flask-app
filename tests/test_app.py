import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'

def test_greet(client):
    name = 'Alice'
    response = client.get(f'/greet/{name}')
    assert response.data == f'Hello, {name}!'.encode()

def test_add(client):
    x, y = 2, 3
    response = client.get(f'/add/{x}/{y}')
    assert response.data == str(x + y).encode()

def test_multiply(client):
    x, y = 2, 3
    response = client.get(f'/multiply/{x}/{y}')
    assert response.data == str(x * y).encode()
