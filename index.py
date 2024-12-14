import os
from flask import Flask, jsonify
import logging
from logging.handlers import RotatingFileHandler

#from src.routes import blueprints


def create_app():

    # Crear app Flask
    app = Flask(__name__)



    # Crear la carpeta "logs" si no existe
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configurar logging
    handler = RotatingFileHandler(
        'logs/app.log', maxBytes=1000000, backupCount=5
    )  # Archivo de log, 1 MB máx., 5 backups
    handler.setLevel(logging.ERROR)  # Registrar solo errores y mayores
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )  # Formato de los logs
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)



    # Registrar todos los blueprints de forma dinámica
    # for bp in blueprints:
    #     app.register_blueprint(bp)

    # Routes
    @app.route('/')
    @app.route('/<name>')
    def index(name=''):
        return f'<h1>Hola mundo desde un café {name}</h1>'

    @app.route('/error')
    def error():
        v = 1 / 0
        return jsonify({"mensaje": "Esto nuna se ejecutará"})




    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f"Error: {str(e)}", exc_info=True)
        return jsonify({"error": "Error interno del servidor"}), 500



    return app




if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)