from http import HTTPStatus

from fast_api.schemas import UserPublic


def test_read_deve_retornar_ok_e_ola_mundo_em_html(client):
    response = client.get('/html/')
    assert response.status_code == HTTPStatus.OK
    html_esperado = """
    <html>
      <head>
        <title>Olá Mundo!</title>
      </head>
      <body>
        <h1>Olá Mundo!</h1>
      </body>
    </html>
    """
    assert response.text == html_esperado


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act - Ação do teste
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá, Mundo'}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


# Exercício 3 da aula 3
def test_get_user_by_id(client, user):
    response = client.get(f'/users/{user.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'matheus',
            'email': 'test@test.com',
            'password': '12345',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


# Exercício 3 - aula 3
def test_get_user_by_id_not_found(client):
    response = client.get('/users/1')

    assert response.json() == {'detail': 'User not found'}


def test_delete_user_not_found(client):
    response = client.delete(
        '/users/2',
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


# Exercício 1 - aula 05
def test_create_user_username_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'Teste',
            'email': 'teste2@test.com',
            'password': 'testtest2',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Username already exists'}


# Exercício 2 - aula 05
def test_create_user_email_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'Teste2',
            'email': 'teste@test.com',
            'password': 'testtest2',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Email already exists'}
