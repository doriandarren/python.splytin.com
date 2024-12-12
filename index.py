from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name = ''):
    return f'<h1>Hola mundo desde un café {name}</h1>'
