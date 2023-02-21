from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return str(x + y)

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    return str(x * y)

if __name__ == '__main__':
    app.run()
