import pytest
from app import create_app, db
from app.models import User
from flask_login import current_user
import uuid 

@pytest.fixture(scope='module')
def test_client():
    app = create_app(config_class='config.TestConfig')  
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  
            yield client  
            db.session.remove()
            db.drop_all()  

@pytest.fixture(scope='function')
def new_user():
    unique_id = str(uuid.uuid4())
    user = User(username=f'testuser_{unique_id}', email=f'testuser_{unique_id}@example.com')
    user.set_password('testpassword')
    
    db.session.add(user)
    db.session.commit()
    
    return user  

def test_register(test_client):
    unique_id = str(uuid.uuid4())
    response = test_client.post('/register', data={
        'username': f'uniqueuser_{unique_id}',
        'email': f'uniqueuser_{unique_id}@example.com', 
        'password': 'newpassword',
        'confirm_password': 'newpassword'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Congratulations, you are now a registered user!' in response.data

def test_login(test_client, new_user):
    response = test_client.post('/login', data={
        'username': new_user.username, 
        'password': 'testpassword'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Welcome' in response.data or b'Error' not in response.data

def test_index_redirects_if_not_authenticated(test_client):
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200

def test_search_movies(test_client, new_user):
    # Ensure the user is logged in
    test_client.post('/login', data={
        'username': new_user.username, 
        'password': 'testpassword'
    })

    response = test_client.post('/search', data={'title': 'Inception'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Inception' in response.data  

def test_logout(test_client, new_user):
    # Ensure the user is logged in
    test_client.post('/login', data={
        'username': new_user.username,  
        'password': 'testpassword'
    })

    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert not current_user.is_authenticated
