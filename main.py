from flask import Flask, render_template

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



if __name__ == '__main__':
    app.run(debug=True, port=5000)
