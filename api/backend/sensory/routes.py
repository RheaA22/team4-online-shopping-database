from flask import Blueprint, request, jsonify

sensory_bp = Blueprint('sensory_bp', __name__)

sensory_products = {
    1: {
        "name": "Soft Magnetic Closure Shirt",
        "brand": "AdaptWear",
        "features": ["Tagless", "Magnetic Closures", "Seamless"],
        "price": 49.99
    },
    2: {
        "name": "Stretchable Formal Pants",
        "brand": "EaseMode",
        "features": ["Stretch Fabric", "Minimal Seams"],
        "price": 79.99
    }
}

# reviews associated with sensory products
sensory_reviews = {
    1: [
        {"userId": 501, "rating": 5, "easeOfUse": 5, "sensoryComfort": 4, "comment": "Super comfy and easy to wear!"}
    ]
}

# GET /sensory/products - get all sensory products
@sensory_bp.route('/sensory/products', methods=['GET'])
def get_all_sensory_products():
    return jsonify(list(sensory_products.values()))

# GET /sensory/products/<id> - get one sensory product
@sensory_bp.route('/sensory/products/<int:product_id>', methods=['GET'])
def get_sensory_product(product_id):
    product = sensory_products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# POST /sensory/products - create a new sensory product
@sensory_bp.route('/sensory/products', methods=['POST'])
def create_sensory_product():
    data = request.json
    new_id = max(sensory_products.keys()) + 1
    sensory_products[new_id] = data
    return jsonify({"message": "Sensory product added", "id": new_id}), 201

# PUT /sensory/products/<id> - update a sensory product
@sensory_bp.route('/sensory/products/<int:product_id>', methods=['PUT'])
def update_sensory_product(product_id):
    if product_id in sensory_products:
        sensory_products[product_id].update(request.json)
        return jsonify({"message": "Sensory product updated"})
    return jsonify({"error": "Product not found"}), 404

# DELETE /sensory/products/<id> - delete a sensory product
@sensory_bp.route('/sensory/products/<int:product_id>', methods=['DELETE'])
def delete_sensory_product(product_id):
    if product_id in sensory_products:
        del sensory_products[product_id]
        return jsonify({"message": "Sensory product deleted"})
    return jsonify({"error": "Product not found"}), 404

# GET /sensory/products/<id>/reviews - get all reviews for a product
@sensory_bp.route('/sensory/products/<int:product_id>/reviews', methods=['GET'])
def get_product_reviews(product_id):
    reviews = sensory_reviews.get(product_id, [])
    return jsonify(reviews)

# POST /sensory/products/<id>/reviews - add a review for a product
@sensory_bp.route('/sensory/products/<int:product_id>/reviews', methods=['POST'])
def add_product_review(product_id):
    data = request.json
    if product_id not in sensory_reviews:
        sensory_reviews[product_id] = []
    sensory_reviews[product_id].append(data)
    return jsonify({"message": "Review added successfully"}), 201

# GET /sensory/products/search - search sensory products
@sensory_bp.route('/sensory/products/search', methods=['GET'])
def search_sensory_products():
    query = request.args.get('feature')
    if not query:
        return jsonify(list(sensory_products.values()))

    filtered = [
        product for product in sensory_products.values()
        if query in product.get("features", [])
    ]
    return jsonify(filtered)
