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


@app.route("/registroProducto", methods=['GET', 'POST'])
def registroProducto():
    if request.method == 'GET':
        return render_template('html/registroProducto.html')


@app.route('/cajeros', methods=['GET', 'POST'])
def cajeros():
    cajeros = [{'id': '1', 'nombre': 'Camila', 'apellido': 'sanchez', 'edad': '20', 'identificacion': '12345',
                'direccion': 'cale123', 'correo': 'lo@lo.com', 'genero': 'Femenino', 'contraseña': '12345', 'imagen': 'imagen'}]
    if request.method == 'GET':
        return render_template('html/usuarios.html', cajeros=cajeros)
    if request.method == 'POST':
        return render_template('html/usuarios.html', cajeros=cajeros)


@app.route('/productos', methods=['GET', 'POST'])
def productos():
    productos = [{'id': '1', 'nombre': 'cafe', 'precio': '1000',
                  'cantidad': '100', 'img': 'img/hot-tea.png'}, {"id": "2", "nombre": "Capuchino", "precio": "2000", "cantidad": "100", 'img': 'img/hot-tea.png'}]
    if request.method == 'GET':
        return render_template('html/productos.html', productos=productos)
    if request.method == 'POST':
        return render_template('html/productos.html', productos=productos)


@app.route('/ventas', methods=['GET'])
def ventas():
    if request.method == 'GET':
        return render_template('html/administrarVenta.html')


if __name__ == '__main__':
    # lanzar el servidor por el puerto
    # debug= true para que se actualicen los cambios en el server
    app.run(port=5000, debug=True)
