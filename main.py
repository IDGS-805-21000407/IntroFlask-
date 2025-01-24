from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/hola')
def hola():
    return 'Hello, world, hola!'



if __name__ == '__main__':
    app.run(debug=True, port=5000)
