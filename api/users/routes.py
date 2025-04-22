from flask import Blueprint, request, jsonify

users_bp = Blueprint('users_bp', __name__)

users = {
    1: {"name": "Alice", "preferences": ["casual"]},
    2: {"name": "Bob", "preferences": ["formal"]}
}


@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))


@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(users.get(user_id, {}))


@users_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_id = max(users.keys()) + 1
    users[new_id] = data
    return jsonify({"message": "User added", "id": new_id}), 201


@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        users[user_id].update(request.json)
        return jsonify({"message": "User updated"})
    return jsonify({"error": "Not found"}), 404


@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "Not found"}), 404
