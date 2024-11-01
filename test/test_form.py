import pytest
from flask import Flask
from werkzeug.security import generate_password_hash
from app import create_app, db  # Adjusted import
from app.models import User  # Adjusted import

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        # Add a test user
        test_user = User(username='test_user', email='test@gmail.com', password=generate_password_hash('password123'))
        db.session.add(test_user)
        db.session.commit()
        yield app
        db.drop_all()

def test_login_get(app):
    client = app.test_client()
    response = client.get("/login")
    assert response.status_code == 200

def test_login_post(app):
    client = app.test_client()
    data = {
        "username": "non_existent_user",
        "password": "password123"
    }
    response = client.post("/login", data=data)
    assert response.status_code == 200

def test_signup_get(app):
    client = app.test_client()
    response = client.get("/signup")
    assert response.status_code == 200

def test_signup_post(app):
    client = app.test_client()
    data = {
        "username": "test_user_new",
        "email": "test_new@gmail.com",
        "password": "password123",
        "confirm": "password123",
    }
    response = client.post("/signup", data=data)
    assert response.status_code == 302
    assert response.headers["Location"] == "/home"

def test_login_check_positive_case(app):
    client = app.test_client()
    data = {
        "username": "test_user",
        "password": "password123",
        "remember": "y",
    }
    response = client.post("/login", data=data)
    assert response.status_code == 302
    assert response.headers["Location"] == "/home_page"
