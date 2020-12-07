from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Pagina principal"


if __name__ == '__main__':
    # lanzar el servidor por el puerto
    # debug= true para que se actualicen los cambios en el server
    app.run(port=5000, debug=True)
