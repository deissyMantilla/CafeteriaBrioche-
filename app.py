from flask import Flask, redirect, url_for, render_template, request
from flask_mail import Mail, Message
import sqlite3
import time

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
        # se verifica si el email esta en la base de datos
        con = sqlite3.connect("brioche.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(
            "select Correo, Contraseña from usuarios where Correo = '"+email+"'")
        respuesta = cur.fetchmany()
        if respuesta:
            correo = respuesta[0][0]
            contrase = respuesta[0][1]
            # se envia correo electronico
            if correo == email:
                msg = Message('Recuperar contraseña Cafeteria Brioche', sender='deissymantilla04@gmail.com',
                              recipients=[email])
                msg.body = "Hola este es un mensaje enviado por la cafeteria Brioche, tu contraseña es: " + \
                    str(contrase)
                mail.send(msg)
                exitoso = 'enviado'

                # Falta poner alerta donde se indique que el correo fue enviado
                return redirect(url_for('loginCajero'))
        else:
            exitoso = 'error'
            return render_template('html/recuperaContrasenia.html', exitoso=exitoso)


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
    if request.method == 'GET':
        con = sqlite3.connect("brioche.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from usuarios")
        cajeros = cur.fetchall()
        return render_template('html/usuarios.html', cajeros=cajeros)
    if request.method == 'POST':
        return render_template('html/usuarios.html', cajeros=cajeros, exitoso="enviado")
    # variable exitoso para activar alerta de confirmacion


@app.route('/productos', methods=['GET', 'POST'])
def productos():
    # Se piden los datos de productos a la base de datos

    if request.method == 'GET':
        productos = peticion()
        return render_template('html/productos.html', productos=productos)
    if request.method == 'POST':
        # se toman los los datos del formulario para enviarlos a la base de datos
        idProducto = request.form['id']
        Nombre = request.form['nombre']
        Precio = request.form['precio']
        Cantidad = request.form['cantidad']
        #URLimagen = request.form['URLimagen']

        # se envian los datos a la base de datos
        with sqlite3.connect("brioche.db") as con:
            try:
                cur = con.cursor()
                cur.execute("update productos set Nombre=' "+Nombre+"', Precio='" +
                            Precio+"', Cantidad='"+Cantidad+"' where id = "+idProducto)
                exito = "enviado"
            except:
                exito = "error"
            finally:
                product = peticion()
                return render_template('html/productos.html', productos=product, exito=exito)

    # variable exito para activar alerta de confirmacion


def peticion():
    con = sqlite3.connect("brioche.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from productos")
    productos = cur.fetchall()
    return productos


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
