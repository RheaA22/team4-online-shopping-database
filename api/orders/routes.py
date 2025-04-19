from flask import Blueprint

orders_bp = Blueprint('orders', __name__)


@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    return {"message": "List of orders"}
