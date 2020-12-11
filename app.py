from flask import Flask, redirect, url_for, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)


# Se configura las propiedades de envio de correos
app.config['DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'deissymantilla04@gmail.com'
app.config['MAIL_PASSWORD'] = 'wylzhjhpycdjzqvj'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


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
        email = request.form['email']
        msg = Message('Recuperar contraseña Cafeteria Brioche', sender='deissymantilla04@gmail.com',
                      recipients=[email])
        msg.body = "Hola este es un mensaje enviado por la cafeteria Brioche, tu contraseña es: "
        mail.send(msg)
        return redirect(url_for('loginCajero'))


@app.route("/registroCajero", methods=['GET', 'POST'])
def registroCajero():
    if request.method == 'GET':
        return render_template('html/registroCajero.html')
    if request.method == 'POST':
        # Registro en base de datos

        # Envio correo electronico con informacion de registro
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['pass']
        msg = Message('Registro - Cafeteria Brioche', sender='deissymantilla04@gmail.com',
                      recipients=[email])
        msg.body = "Hola " + nombre + ", este es un mensaje enviado por la cafeteria Brioche, has sido registrado con cajero en la cafeteria.  Tu usuario es: " + \
            email+" y tu contraseña es: "+password
        mail.send(msg)
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
        return render_template('html/usuarios.html', cajeros=cajeros, exitoso="enviado")
    # variable exitoso para activar alerta de confirmacion


@app.route('/productos', methods=['GET', 'POST'])
def productos():
    productos = [{'id': '1', 'nombre': 'cafe', 'precio': '1000',
                  'cantidad': '100', 'img': 'img/hot-tea.png'}, {"id": "2", "nombre": "Capuchino", "precio": "2000", "cantidad": "100", 'img': 'img/hot-tea.png'}]
    if request.method == 'GET':
        return render_template('html/productos.html', productos=productos)
    if request.method == 'POST':
        # envio a db
        return render_template('html/productos.html', productos=productos, exito="enviado")
    # variable exito para activar alerta de confirmacion


@app.route('/ventas', methods=['GET', 'POST'])
def ventas():
    if request.method == 'GET':
        return render_template('html/administrarVenta.html')
    if request.method == 'POST':
        return render_template('html/administrarVenta.html')


@app.route('/balance', methods=['GET'])
def balance():
    return render_template('html/balance.html')


if __name__ == '__main__':
    # lanzar el servidor por el puerto
    # debug= true para que se actualicen los cambios en el server
    app.run(port=5000, debug=True)
