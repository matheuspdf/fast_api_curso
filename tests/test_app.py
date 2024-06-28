from http import HTTPStatus


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
        '/users/',  # UserSchema
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}
