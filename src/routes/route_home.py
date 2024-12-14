from flask import Blueprint, jsonify


home_bp = Blueprint('home', __name__, url_prefix='/')


# Routes
@home_bp.route('/')
@home_bp.route('/<name>')
def index(name = ''):
    return f'<h1>Hola mundo desde un café {name}</h1>'


@home_bp.route('/error')
def error():
    v = 1 / 0
    return jsonify({"mensaje": "Esto nuna se ejecutará"})