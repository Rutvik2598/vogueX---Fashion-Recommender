# tests/conftest.py

import pytest
from app import db  # Adjust if create_app is defined in app.py

@pytest.fixture(scope='module')
def test_client():
    # Create the app with testing configurations
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Establish an application context before running the tests
    with flask_app.app_context():
        db.create_all()  # Set up tables for testing
        yield flask_app.test_client()  # Provide the test client
        db.drop_all()  # Clean up after tests
