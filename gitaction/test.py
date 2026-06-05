import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_page_loads(client):
    """Test that the login page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Login" in response.data or b"login" in response.data

def test_login_success(client):
    """Test login with valid credentials (redirects to dashboard)."""
    response = client.post('/login', data={
        'username': 'student1',
        'password': '1234'
    })
    assert response.status_code == 302
    assert '/dashboard/student1' in response.headers['Location']

def test_login_failure(client):
    """Test login with invalid credentials."""
    response = client.post('/login', data={
        'username': 'student1',
        'password': 'wrongpassword'
    })
    assert response.status_code == 200
    assert b"Invalid credentials" in response.data

def test_dashboard_page(client):
    """Test that the dashboard page loads for a user."""
    response = client.get('/dashboard/student1')
    assert response.status_code == 200
    assert b"student1" in response.data