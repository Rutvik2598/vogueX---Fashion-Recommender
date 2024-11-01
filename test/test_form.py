import pytest
from app import app # Make sure to import your Flask app
from flask import Flask

# Fixture to create a test instance of the app
@pytest.fixture
def app():
    app = Flask(__name__, static_folder='static')  # Create your Flask app instance
    yield app  # Yield the app instance for use in tests

# Fixture to create a test client for the app
@pytest.fixture
def client(app):
    return app.test_client()  # Return the test client

def test_login_get(client):
    response = client.get('/login')  # Use the client to make a request
    assert response.status_code == 200  # Check if the response is OK

def test_login_post(client):
    response = client.post('/login', data={'username': 'test', 'password': 'test'})
    assert response.status_code == 200  # Check for successful login

def test_signup_get(client):
    response = client.get('/signup')
    assert response.status_code == 200  # Check if the signup page loads

def test_signup_post(client):
    response = client.post('/signup', data={'username': 'test', 'password': 'test'})
    assert response.status_code == 200  # Check for successful signup

def test_login_check_positive_case(client):
    response = client.post('/login', data={'username': 'valid_user', 'password': 'valid_password'})
    assert response.status_code == 200  # Check for successful login with valid credentials
