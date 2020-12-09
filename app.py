from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('html/index.html')


@app.route("/loginAdmin", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('html/loginAdmin.html')
    if request.method == 'POST':
        return redirect(url_for('productos'))


@app.route("/loginCajero", methods=['GET', 'POST'])
def loginCajero():
    if request.method == 'GET':
        return render_template('html/loginCajero.html')
    if request.method == 'POST':
        return redirect(url_for('ventas'))


@app.route("/recuperarPass", methods=['GET', 'POST'])
def recuperarPass():
    if request.method == 'GET':
        return render_template('html/recuperaContrasenia.html')
    if request.method == 'POST':
        return redirect(url_for('loginCajero'))


@app.route("/registroCajero", methods=['GET', 'POST'])
def registroCajero():
    if request.method == 'GET':
        return render_template('html/registroCajero.html')


@app.route('/cajeros', methods=['GET', 'POST'])
def cajeros():
    if request.method == 'GET':
        return render_template('html/usuarios.html')
    if request.method == 'POST':
        return render_template('html/usuarios.html')


@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'GET':
        return render_template('html/productos.html')
    if request.method == 'POST':
        return render_template('html/productos.html')


@app.route('/ventas', methods=['GET'])
def ventas():
    if request.method == 'GET':
        return render_template('html/administrarVenta.html')


if __name__ == '__main__':
    # lanzar el servidor por el puerto
    # debug= true para que se actualicen los cambios en el server
    app.run(port=5000, debug=True)
