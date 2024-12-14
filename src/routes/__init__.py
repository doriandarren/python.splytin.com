from src.routes.route_employees import employee_bp
from src.routes.route_customers import customer_bp
from src.routes.route_home import home_bp


# Lista de blueprints
blueprints = [
    employee_bp,
    customer_bp,
    home_bp
]