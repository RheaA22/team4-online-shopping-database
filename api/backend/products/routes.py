from flask import Blueprint, request, jsonify
from backend.ml_models.model_products import predict as predict_product


products_bp = Blueprint('products_bp', __name__)

products = {
    1: {"name": "T-shirt", "price": 19.99, "stock": True, "category": "general"},
    2: {"name": "Jeans", "price": 49.99, "stock": True, "category": "general"},
    3: {
        "name": "Soft Magnetic Closure Shirt",
        "brand": "AdaptWear",
        "features": ["Tagless", "Magnetic Closures", "Seamless"],
        "price": 49.99,
        "stock": True,
        "category": "sensory"
    },
    4: {
        "name": "Stretchable Formal Pants",
        "brand": "EaseMode",
        "features": ["Stretch Fabric", "Minimal Seams"],
        "price": 79.99,
        "stock": True,
        "category": "sensory"
    },
    5: {
        "name": "Organic Cotton Hoodie",
        "brand": "GreenThreads",
        "features": ["Organic Cotton", "Eco-Friendly Dyes", "Sustainable"],
        "price": 59.99,
        "stock": True,
        "category": "sustainable"
    }
}

# reviews only for sensory products
product_reviews = {
    3: [
        {
            "userId": 501,
            "rating": 5,
            "easeOfUse": 5,
            "sensoryComfort": 4,
            "comment": "Super comfy and easy to wear!"
        }
    ]
}

# GET /products - all products
@products_bp.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(list(products.values()))

# GET /products/<id> - one product
@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# GET /products/instock - in-stock products
@products_bp.route('/products/instock', methods=['GET'])
def get_instock_products():
    instock = [p for p in products.values() if p.get('stock')]
    return jsonify(instock)

# GET /products/category/<cat> - products by category
@products_bp.route('/products/category/<category>', methods=['GET'])
def get_by_category(category):
    filtered = [p for p in products.values() if p.get('category') == category]
    return jsonify(filtered)

# POST /products/search - search by keyword in name
@products_bp.route('/products/search', methods=['POST'])
def search_products():
    keyword = request.json.get("keyword", "").lower()
    results = [p for p in products.values() if keyword in p['name'].lower()]
    return jsonify(results)

# GET /products/search/features?feature=...
@products_bp.route('/products/search/features', methods=['GET'])
def search_by_feature():
    query = request.args.get('feature')
    if not query:
        return jsonify(list(products.values()))
    filtered = [
        p for p in products.values()
        if 'features' in p and query in p['features']
    ]
    return jsonify(filtered)

# POST /products - add new product
@products_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_id = max(products.keys()) + 1
    data['stock'] = data.get('stock', True)
    data['category'] = data.get('category', 'general')
    products[new_id] = data
    return jsonify({"message": "Product added", "id": new_id}), 201

# PUT /products/<id> - update product
@products_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id in products:
        products[product_id].update(request.json)
        return jsonify({"message": "Product updated"})
    return jsonify({"error": "Product not found"}), 404

# DELETE /products/<id> - mark out of stock
@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
def mark_out_of_stock(product_id):
    if product_id in products:
        products[product_id]['stock'] = False
        return jsonify({"message": "Marked out of stock"})
    return jsonify({"error": "Product not found"}), 404

# GET /products/<id>/reviews - reviews for sensory products
@products_bp.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews(product_id):
    reviews = product_reviews.get(product_id, [])
    return jsonify(reviews)

# POST /products/<id>/reviews - add review to sensory product
@products_bp.route('/products/<int:product_id>/reviews', methods=['POST'])
def add_review(product_id):
    if product_id not in product_reviews:
        product_reviews[product_id] = []
    product_reviews[product_id].append(request.json)
    return jsonify({"message": "Review added successfully"}), 201

# PREDICT - ML model prediction
@products_bp.route('/products/predict/<price>/<feature_count>', methods=['GET'])
def predict_product_value(price, feature_count):
    current_app.logger.info(f'Predicting for price={price} and feature_count={feature_count}')

    prediction = predict_product(price, feature_count)
    return jsonify({"prediction_result": prediction}), 200
