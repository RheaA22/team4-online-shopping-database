from flask import Blueprint, request, jsonify

orders_bp = Blueprint('orders_bp', __name__)

orders = {
    1: {"user_id": 1, "items": [1, 2], "status": "pending"},
    2: {"user_id": 2, "items": [2], "status": "shipped"}
}


@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(list(orders.values()))


@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return jsonify(orders.get(order_id, {}))


@orders_bp.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    new_id = max(orders.keys()) + 1
    orders[new_id] = data
    return jsonify({"message": "Order created", "id": new_id}), 201


@orders_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    if order_id in orders:
        orders[order_id].update(request.json)
        return jsonify({"message": "Order updated"})
    return jsonify({"error": "Order not found"}), 404


@orders_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def cancel_order(order_id):
    if order_id in orders:
        del orders[order_id]
        return jsonify({"message": "Order cancelled"})
    return jsonify({"error": "Order not found"}), 404
