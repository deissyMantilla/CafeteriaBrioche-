from flask import Flask, redirect, url_for, render_template, request, session
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
import sqlite3
import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'brioche123'

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


@app.route("/loginAdmin", defaults={'exitoso': None}, methods=['GET', 'POST'])
@app.route("/loginAdmin/<exitoso>", methods=['GET', 'POST'])
def login(exitoso):
    if request.method == 'GET':
        return render_template('html/loginAdmin.html', exitoso=exitoso)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        correoAdmin = 'admin@gmail.com'
        passAdmin = 'Brioche_admin'
        if username == correoAdmin and password == passAdmin:
            session['username'] = username
            session['rol'] = 'admin'
            return redirect(url_for('productos'))
        else:
            exitoso = 'noRegistrado'
            return render_template('html/loginAdmin.html', exitoso=exitoso)
        # Falta validar la contraseña


@app.route("/loginCajero", defaults={'exitoso': None}, methods=['GET', 'POST'])
@app.route("/loginCajero/<exitoso>", methods=['GET', 'POST'])
def loginCajero(exitoso):
    if request.method == 'GET':
        print(exitoso)
        return render_template('html/loginCajero.html', exitoso=exitoso)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        con = sqlite3.connect("brioche.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(
            "select Correo, Contraseña from usuarios where Correo = '"+username+"'")
        respuesta = cur.fetchmany()
        if respuesta:
            contrase = respuesta[0][1]
            if bcrypt.check_password_hash(contrase, password):
                session['username'] = username
                session['rol'] = 'cajero'
                return redirect(url_for('ventas'))
            else:
                exitoso = 'noRegistrado'
                return render_template('html/loginCajero.html', exitoso=exitoso)
        else:
            print('error')
        # Falta validar la contraseña


@app.route("/recuperarPass", defaults={'exitoso': None}, methods=['GET', 'POST'])
@app.route("/recuperarPass/<exitoso>", methods=['GET', 'POST'])
def recuperarPass(exitoso):
    if request.method == 'GET':
        return render_template('html/recuperaContrasenia.html', exitoso=exitoso)
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
                # se redirige a la pagina de login
                return redirect(url_for('loginCajero', exitoso=exitoso))
        else:
            exitoso = 'error'
            # si hay un error se vuelve a cargar la pagina de recuperar contraseña pero con una alerta de error
            return redirect(url_for('recuperarPass', exitoso=exitoso))


@app.route("/registroCajero", defaults={'exito': None}, methods=['GET', 'POST'])
@app.route("/registroCajero/<exito>", methods=['GET', 'POST'])
def registroCajero(exito):
    if 'username' in session and session['rol'] == 'admin':
        if request.method == 'GET':
            return render_template('html/registroCajero.html', exito=exito)
        if request.method == 'POST':

            # Registro en base de datos
            with sqlite3.connect("brioche.db") as con:
                try:
                    nombre = request.form["nombre"]
                    apellido = request.form["apellido"]
                    correo = request.form["email"]
                    edad = request.form["edad"]
                    identificacion = request.form["identificacion"]
                    direccion = request.form["direccion"]
                    genero = request.form["genero"]
                    contraseña = request.form["pass"]
                    pw_hash = bcrypt.generate_password_hash(contraseña)
                    # URLimagen = request.form["URLimagen"]
                    cur = con.cursor()

                    cur.execute("INSERT INTO usuarios (Nombre, Apellido, Correo, Edad, Identificacion, Direccion, Genero,Contraseña) VALUES (?,?,?,?,?,?,?,?)",
                                (nombre, apellido, correo, edad, identificacion, direccion, genero, pw_hash))
                    con.commit()
                    exito = 'enviado'
                    # Envio correo electronico con informacion de registro
                    nombre = request.form['nombre']
                    email = request.form['email']
                    password = request.form['pass']
                    msg = Message('Registro - Cafeteria Brioche',
                                  sender='deissymantilla04@gmail.com', recipients=[email])
                    msg.body = "Hola " + nombre + ", este es un mensaje enviado por la cafeteria Brioche, has sido registrado como cajero en la cafeteria.  Tu usuario es: " + \
                        email+" y tu contraseña es: "+password
                    mail.send(msg)
                except:
                    exito = 'error'
                finally:
                    return redirect(url_for('registroCajero', exito=exito))
    elif 'username' in session:
        return redirect(url_for('ventas'))
    else:
        return redirect(url_for('home'))


@app.route("/registroProducto", defaults={'exito': None}, methods=['GET', 'POST'])
@app.route("/registroProducto/<exito>", methods=['GET', 'POST'])
def registroProducto(exito):
    if 'username' in session and session['rol'] == 'admin':
        if request.method == 'GET':
            return render_template('html/registroProducto.html', exito=exito)
        if request.method == 'POST':
            with sqlite3.connect("brioche.db") as con:
                try:
                    nombre = request.form["nombre"]
                    precio = request.form["precio"]
                    cantidad = request.form["cantidad"]
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO productos (nombre, precio,cantidad) VALUES ('"+nombre+"','"+precio+"','"+cantidad+"')")
                    con.commit()
                    exito = 'enviado'
                except:
                    exito = 'error'
                finally:
                    return redirect(url_for('registroProducto', exito=exito))
    elif 'username' in session:
        return redirect(url_for('ventas'))
    else:
        return redirect(url_for('home'))


@app.route('/cajeros', defaults={'exito': None, 'idP': None}, methods=['GET', 'POST'])
@app.route('/cajeros/<exito>', defaults={'idP': None}, methods=['GET', 'POST'])
@app.route('/cajeros/<idP>', defaults={'exito': None}, methods=['GET', 'POST'])
def cajeros(exito, idP):
    if 'username' in session and session['rol'] == 'admin':
        if request.method == 'GET':
            if idP:
                with sqlite3.connect("brioche.db") as con:
                    try:
                        cur = con.cursor()
                        cur.execute("delete from usuarios where id = ?", idP)
                    except:
                        exito = 'error'
                    finally:
                        return redirect(url_for('cajeros'))

            else:
                con = sqlite3.connect("brioche.db")
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute("select * from usuarios")
                cajeros = cur.fetchall()
                return render_template('html/usuarios.html', cajeros=cajeros, exito=exito)
        if request.method == 'POST':
            # se traen los datos del formulario
            idUsuario = request.form['idForm']
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            edad = request.form['edad']
            identificacion = request.form['identificacion']
            direccion = request.form['direccion']
            email = request.form['email']
            genero = request.form['genero']
            password = request.form['password']
            # queda pendiente la imagen

            # se envian los datos a la base de datos
            with sqlite3.connect("brioche.db") as con:
                try:
                    cur = con.cursor()
                    cur.execute("update usuarios set Nombre=?, Apellido=?, Edad=?, Identificacion=?,Genero=?, Correo=?, Contraseña=?, Direccion=? where id=?",
                                (nombre, apellido, edad, identificacion, genero, email, password, direccion, idUsuario))
                    con.commit()
                    exito = "enviado"
                except:
                    exito = "error"
                finally:
                    return redirect(url_for('cajeros', exito=exito))
    elif 'username' in session:
        return redirect(url_for('ventas'))
    else:
        return redirect(url_for('home'))
    # variable exitoso para activar alerta de confirmacion


@app.route('/productos', defaults={'exito': None, 'idP': None}, methods=['GET', 'POST'])
@app.route('/productos/<exito>', defaults={'idP': None},  methods=['GET', 'POST'])
@app.route('/productos/<idP>', defaults={'exito': None}, methods=['GET', 'POST'])
def productos(exito, idP):
    # se valida el rol de la sesion
    if 'username' in session and session['rol'] == 'admin':
        print('la sesion esta con admin')
        # Se piden los datos de productos a la base de datos
        if request.method == 'GET':
            if idP:
                with sqlite3.connect("brioche.db") as con:
                    try:
                        cur = con.cursor()
                        cur.execute("delete from productos where id = ?", idP)
                    except:
                        exito = 'error'
                    finally:
                        return redirect(url_for('productos'))
            else:
                con = sqlite3.connect("brioche.db")
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute("select * from productos")
                productos = cur.fetchall()
                return render_template('html/productos.html', productos=productos, exito=exito)
        if request.method == 'POST':
            # se toman los los datos del formulario para enviarlos a la base de datos
            idProducto = request.form['id']
            Nombre = request.form['nombre']
            Precio = request.form['precio']
            Cantidad = request.form['cantidad']
            # URLimagen = request.form['URLimagen']

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
                    return redirect(url_for('productos', exito=exito))
    elif 'username' in session:
        return redirect(url_for('ventas'))
    else:
        return redirect(url_for('home'))
    # variable exito para activar alerta de confirmacion


@app.route('/ventas', methods=['GET', 'POST'])
def ventas():
    if 'username' in session:
        if request.method == 'GET':
            con = sqlite3.connect("brioche.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from productos")
            productos = cur.fetchall()
            return render_template('html/administrarVenta.html', productos=productos)
        if request.method == 'POST':
            return render_template('html/administrarVenta.html')
    else:
        return redirect(url_for('home'))

def formatearFecha(date):
  year = date.strftime("%Y")
  month = date.strftime("%m")
  day = date.strftime("%d")
  return day + "-" + month + "-" + year

def obtenerFechaActual():
    x = datetime.datetime.now()    
    return formatearFecha(x)

@app.route('/balance/<fecha>', defaults={'fecha': obtenerFechaActual()}, methods=['GET'])
def balance(fecha):
    if 'username' in session and session['rol'] == 'admin':
        con = sqlite3.connect("brioche.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from ventas where fecha = '" + fecha +"'")
        ventas = cur.fetchall()
        cur.execute("select sum(total) from ventas where fecha = '" + fecha +"'")
        balance = cur.fetchone()
        return render_template('html/balance.html', ventas = ventas, balance = balance[0])
    elif 'username' in session:
        return redirect(url_for('ventas'))
    else:
        return redirect(url_for('home'))


@app.route("/cerrarSesion", methods=['GET'])
def cerrarSesion():
    if 'username' in session:
        session.pop('username')
        session.pop('rol')
    return redirect(url_for('home'))


if __name__ == '__main__':
    # lanzar el servidor por el puerto
    # debug= true para que se actualicen los cambios en el server
    app.run(port=5000, debug=True)
