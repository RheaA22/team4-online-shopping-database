from flask import Blueprint, request, jsonify

categories_bp = Blueprint('categories_bp', __name__)

categories = {
    1: {"name": "Summer Wear"},
    2: {"name": "Winter Wear"}
}


@categories_bp.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(list(categories.values()))


@categories_bp.route('/categories/<int:cat_id>', methods=['GET'])
def get_category_products(cat_id):
    return jsonify({"products": [f"Sample product in category {cat_id}"]})


@categories_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    new_id = max(categories.keys()) + 1
    categories[new_id] = data
    return jsonify({"message": "Category added", "id": new_id}), 201


@categories_bp.route('/categories/<int:cat_id>', methods=['PUT'])
def update_category(cat_id):
    if cat_id in categories:
        categories[cat_id].update(request.json)
        return jsonify({"message": "Category updated"})
    return jsonify({"error": "Category not found"}), 404


@categories_bp.route('/categories/<int:cat_id>', methods=['DELETE'])
def delete_category(cat_id):
    if cat_id in categories:
        del categories[cat_id]
        return jsonify({"message": "Category deleted"})
    return jsonify({"error": "Not found"}), 404
