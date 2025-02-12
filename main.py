from flask import Flask, render_template
from flask import Flask, request
from flask import Flask, render_template, request, url_for 
from flask import Flask, render_template, request



app = Flask(__name__)

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


@app.route('/resultado', methods=["GET","POST"])
def result():
    if request.method == 'POST':
        num1 = request.form.get('n1')
        num2 = request.form.get('n2')
        return "La multiplicacion de {} y {} es {}".format(num1, num2, str(int(num1)*int(num2)))
    
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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
