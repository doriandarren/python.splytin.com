from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Prueba 2 para todo el mundo'

if __name__ == '__main__':
    app.run()