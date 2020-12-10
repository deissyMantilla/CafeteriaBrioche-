from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('html/index.html')


@app.route('/cajeros', methods=['GET'])
def cajeros():
    if request.method == 'GET':
        return render_template('html/usuarios.html')


@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'GET':
        return render_template('html/productos.html')
    if request.method == 'POST':
        return 'Cambio guardado con exito'

@app.route('/balance/<string:fecha_balance>/')
def balance(fecha_balance):
    return render_template('html/balance.html', fecha_balance = fecha_balance)


if __name__ == '__main__':
    # lanzar el servidor por el puerto
    # debug= true para que se actualicen los cambios en el server
    app.run(port=5000, debug=True)
