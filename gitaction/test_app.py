
import pytest
# 1. This explicitly tells Python: Go into 'app' folder, open 'app.py', and grab the 'app' variable
from app.app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Below this line, your tests remain exactly the same!
def test_login_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200

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