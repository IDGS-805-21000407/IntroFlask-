from flask import Flask, render_template
from flask import Flask, request
from flask import Flask, render_template, request, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, request
from datetime import datetime
import forms
from flask import g

app = Flask(__name__)
app.secret_key = "secret"
csrf=CSRFProtect()

@app.route('/')
def index():
    titulo="IDGS805"
    lista=['pedro','juan','mario']
    return render_template('index.html', titulo=titulo, lista=lista)


@app.route('/ejemplo1')
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')
def ejemplo2():
    return render_template('ejemplo2.html')

@app.route('/hola')
def hola():
    return '<h1>Hello, world, hola!</h1>'

@app.route('/user/<string:user>')
def user(user):
    return f"Hola, {user}!"

@app.route('/user/<int:n>')
def numero(n):
    return f"El numero es: {n}"

@app.route('/user/<int:id>/<string:username>')
def username(id, username): 
    return f"El usuario : {username}, tu ID es {id}"

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f"La suma es: {n1+n2}"

@app.route('/default/')
@app.route('/default/<string:temp>/')
def func1(temp='YOOO'):
    return f"Hola, {temp}"


@app.route('/form1')
def form1():
    return '''
    <form>
        <label for="nombre">Name:</label>
        <input type="text" id"nombre" placeholder="Name">
    </form>
    '''      
    
@app.route('/OperaBas')
def OperaBas():
    return render_template('OperaBas.html')


@app.route('/resultado', methods=["POST"])
def result():
    num1 = request.form.get('n1', type=int)
    num2 = request.form.get('n2', type=int)
    operacion = request.form.get('operacion')
    
    operaciones = {
        "suma": num1 + num2,
        "resta": num1 - num2,
        "multiplicacion": num1 * num2,
        "division": "No se puede dividir por cero" if num2 == 0 else num1 / num2
    }
    
    resultado = operaciones.get(operacion, "Operación no válida")
    return f"El resultado de la {operacion} de {num1} y {num2} es {resultado}"


#Cinepolis

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidadPersonasVenta = 0
        self.boletos = 0
        self.metodoPago = ""
        self.total = 0
        
    def asignarCompra(self, cantidadPersonasVenta, boletos):
        self.cantidadPersonasVenta = cantidadPersonasVenta
        self.boletos = boletos
    
    def calcularTotal(self):
        precio = 12.00
        total = self.boletos * precio
        if self.boletos > 5:
            total *= 0.85  # 15% de descuento
        elif self.boletos > 3:
            total *= 0.90  # 10% de descuento
        self.total = total
        return total
        
    def aplicarDescuentoTarjeta(self):
        self.total *= 0.90  # Descuento adicional del 10% por tarjeta CINECO
            
    def __str__(self):
        return f"{self.nombre}, {self.total:.2f}"
    
class Boleto:
    Cantidad_Boleto_Max_Persona = 7

    def validarCantidadBoletos(cantidadPersonasVenta, boletos):
        return boletos <= cantidadPersonasVenta * Boleto.Cantidad_Boleto_Max_Persona
    
@app.route('/Cinepolis', methods=["GET", "POST"])
def Cinepolis():
    total_pagar = None
    error = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad_compradores = int(request.form["compradores"])
        boletos = int(request.form["boletas"])
        cineco = request.form["cineco"]

        if not Boleto.validarCantidadBoletos(cantidad_compradores, boletos):
            error = "No puedes comprar más de 7 boletos por persona."
            return render_template("Cinepolis.html", error=error, total_pagar=None, nombre=nombre, compradores=cantidad_compradores, boletas=boletos, cineco=cineco)

        cliente = Persona(nombre)
        cliente.asignarCompra(cantidad_compradores, boletos)
        total_pagar = cliente.calcularTotal()

        if cineco == "si":
            cliente.aplicarDescuentoTarjeta()
            total_pagar = cliente.total

    return render_template("Cinepolis.html", total_pagar=total_pagar, error=error)



@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    print("alumno:{}".format(g.nombre))
    mat = ''
    nom = ''
    ape = ''
    email = ''
    alumno_clase=forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clase.validate():
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data
        #print("Nombre: {}".format(nom))
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos.html", form=alumno_clase, mat=mat, nom=nom, ape=ape, email=email)

signos_zodiaco_chino = [
    "monkey", "rooster", "dog", "pig", "rat", "bull",
    "tiger", "rabbit", "dragon", "snake", "horse", "sheep"  
]

def obtener_signo_chino(anio):
    return signos_zodiaco_chino[anio % 12]

@app.route('/Zodiaco', methods=['GET', 'POST'])
def zodiaco():
    nombre = ''
    amaterno = ''
    apaterno = ''
    edad = None
    signo = ''
    imagen_signo = ''
    form = forms.UserFormZodiaco(request.form)
    if request.method == 'POST' and form.validate():
        nombre = form.nombre.data
        amaterno = form.amaterno.data
        apaterno = form.apaterno.data
        dia = int(form.dia.data)
        mes = int(form.mes.data)
        anio = int(form.anio.data)
        hoy = datetime.today()
        edad = hoy.year - anio - ((hoy.month, hoy.day) < (mes, dia))
        signo = obtener_signo_chino(anio)
        imagen_signo = f"img/{signo}.png"
    return render_template("Zodiacochino.html", form=form, nombre=nombre, 
                           amaterno=amaterno, apaterno=apaterno, 
                           edad=edad, signo=signo, imagen_signo=imagen_signo)
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    g.nombre="Pedro"
    print("Before 1")
    
@app.after_request
def after_request(response):
    print("After 1")
    return response
        
    
if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, port=5000)
