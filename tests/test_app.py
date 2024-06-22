from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange - Organização do teste
    response = client.get('/')  # Act - Ação do teste
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá, Mundo'}


def test_read_deve_retornar_ok_e_ola_mundo_em_html():
    client = TestClient(app)
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
