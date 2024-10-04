from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Prueba que todo funcione bien!!'

if __name__ == '__main__':
    app.run()