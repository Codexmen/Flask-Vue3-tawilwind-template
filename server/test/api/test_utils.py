import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app(config_name='test')
    return app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_ping(client):
    response = client.get('/')
    print(response)
    assert response.status_code == 200


def test_utils_me(app, client):
    response = client.get('/api/auth/me')
    assert response.status_code == 200
    assert response.json['username'] == ''


def test_utils_login_with_wrong_creds(app, client):
    response = client.post('/api/auth/login', json={"email": "admin@admin.com", "password": "qwe1qwe"})
    assert response.status_code == 200
    assert response.json['isAuthenticated'] == False


def test_utils_login_successful(app, client):
    response = client.post('/api/auth/login', json={"email": "admin@admin.com", "password": "qwe123"})
    assert response.status_code == 200
    assert response.json['isAuthenticated'] == True
    assert response.json['email'] == 'admin@admin.com'


def test_utils_register_wrong_email(app, client):
    response = client.post('/api/auth/register', json={"email": "", "password": ""})
    assert response.status_code == 400
    assert response.json == {"error": '{\'email\': [\'Not a valid email address.\']}'}


def test_utils_register_wrong_password(app, client):
    response = client.post('/api/auth/register', json={"email": "abc@abc.com"})
    assert response.status_code == 400
    assert response.json == {'error': "{'password': ['Missing data for required field.']}"}


def test_utils_register_exist_user(app, client):
    response = client.post('/api/auth/register', json={"email": "admin@admin.com", "password": "qwe123"})
    assert response.status_code == 400
    assert response.json == {'code': 501, 'error': 'user exist'}


def test_logout(app, client):
    response = client.post('/api/auth/login', json={"email": "admin@admin.com", "password": "qwe123"})
    assert response.json['isAuthenticated'] is True
    assert response.json['email'] == 'admin@admin.com'
    response = client.get('/api/auth/me')
    assert response.status_code == 200
    assert response.json['username'] == 'admin@admin.com'
    response = client.post('/api/auth/logout')
    assert response.status_code == 200
    response = client.get('/api/auth/me')
    assert response.status_code == 200
    assert response.json['username'] == ''
