from http import HTTPStatus

from fastapi import FastAPI
from starlette.responses import HTMLResponse

from fast_api.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo'}


@app.get('/html/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_deve_retornar_ok_e_ola_mundo_em_html():
    conteudo_html = """
    <html>
      <head>
        <title>Olá Mundo!</title>
      </head>
      <body>
        <h1>Olá Mundo!</h1>
      </body>
    </html>
    """
    return conteudo_html
