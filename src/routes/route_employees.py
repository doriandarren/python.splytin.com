from flask import Blueprint, jsonify

# Crear un blueprint para empleados
employee_bp = Blueprint('employees', __name__, url_prefix='/employees')

@employee_bp.route('/')
def list_employees():
    return jsonify({"message": "Listado de empleados"})

@employee_bp.route('/<int:id>')
def get_employee(id):
    return jsonify({"message": f"Información del empleado {id}"})