from flask import Flask, g
import json
from website.auth import auth
from website.auth import db
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sys

sys.path.append("..")


def test_login_get(app):
    client = app.test_client()
    url = "/login"

    response = client.get(url)
    assert response.status_code == 200  # Check if the login page loads successfully


def test_login_post(app):
    client = app.test_client()
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    # Adjusted to use username instead of email, as per app expectations
    data = {
        "username": "non_existent_user",  # This user should not be in the database
        "password": "password123"
    }
    url = "/login"

    response = client.post(url, data=data, headers=headers)
    assert response.status_code == 200  # Expect the login page to reload with error message


def test_signup_get(app):
    client = app.test_client()
    url = "/signup"  # Adjusted to match the actual signup route
    response = client.get(url)
    assert response.status_code == 200  # Check if the signup page loads successfully



def test_signup_post(app):
    client = app.test_client()
    url = "/signup"
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    data = {
        "username": "test_user",
        "email": "test@gmail.com",
        "password": "password123",
        "confirm": "password123",
    }

    response = client.post(url, data=data, headers=headers)
    assert response.status_code == 302  # Expect a redirect on successful signup
    assert response.headers["Location"] == "/home"  # Check if redirected to /home


def test_login_check_positive_case(app):
    client = app.test_client()
    url = "/login"
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    # Ensure a test user is created beforehand or use a setup fixture
    data = {
        "username": "test_user",  # Replace with actual username if different
        "password": "password123",
        "remember": "y",  # Assuming 'remember' can be "y" for True; omit if unnecessary
    }

    response = client.post(url, data=data, headers=headers)
    assert response.status_code == 302  # Expect redirect on successful login
    assert response.headers["Location"] == "/home_page"  # Check if redirected to home page
