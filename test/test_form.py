import pytest
from app import create_app, db , User 
from flask import url_for
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    app = create_app('testing')  # Create your app instance
    with app.app_context():
        db.create_all()  # Create the test database
        test_user = User(username="testuser", email="vedanttp1210@gmail.com", password=generate_password_hash("password123"))
        db.session.add(test_user)
        db.session.commit()
        yield app
        db.drop_all()  # Clean up after tests

@pytest.fixture
def client(app):
    return app.test_client() 

def test_login_get(client):
    response = client.get('/login')  # Use the client to make a request
    assert response.status_code == 200  # Check if the response is OK

def test_login_post(client):
    response = client.post('/login', data={'username': 'smi', 'password': 'test'})
    assert response.status_code == 200  # Check for successful login

def test_signup_get(client):
    response = client.get('/signup')
    assert response.status_code == 200  # Check if the signup page loads

def test_signup_post(client):
    response = client.post('/signup', data={'username': 'smi', 'email': 'skothar3@ncsu.edu', 'password': 'test', 'confirm':'test'})
    assert response.status_code == 200  # Check for successful signup

def test_login_check_positive_case(client):
    response = client.post('/login', data={'username': 'valid_user', 'password': 'valid_password'})
    assert response.status_code == 200  # Check for successful login with valid credentials
