from flask import Blueprint, jsonify

# Crear un blueprint para clientes
customer_bp = Blueprint('customers', __name__, url_prefix='/customers')

@customer_bp.route('/')
def list_customers():
    return jsonify({"message": "Listado de clientes"})

@customer_bp.route('/<int:id>')
def get_customer(id):
    return jsonify({"message": f"Información del cliente {id}"})
