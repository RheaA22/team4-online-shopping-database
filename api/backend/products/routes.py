from flask import Blueprint, request, jsonify

products_bp = Blueprint('products_bp', __name__)

products = {
    1: {"name": "T-shirt", "price": 19.99, "stock": True},
    2: {"name": "Jeans", "price": 49.99, "stock": True}
}


@products_bp.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(list(products.values()))


@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify(products.get(product_id, {}))


@products_bp.route('/products/instock', methods=['GET'])
def get_instock_products():
    instock = [p for p in products.values() if p['stock']]
    return jsonify(instock)


@products_bp.route('/products/search', methods=['POST'])
def search_products():
    keyword = request.json.get("keyword", "").lower()
    results = [p for p in products.values() if keyword in p['name'].lower()]
    return jsonify(results)


@products_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_id = max(products.keys()) + 1
    products[new_id] = data
    return jsonify({"message": "Product added", "id": new_id}), 201


@products_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id in products:
        products[product_id].update(request.json)
        return jsonify({"message": "Product updated"})
    return jsonify({"error": "Product not found"}), 404


@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
def mark_out_of_stock(product_id):
    if product_id in products:
        products[product_id]['stock'] = False
        return jsonify({"message": "Marked out of stock"})
    return jsonify({"error": "Product not found"}), 404
