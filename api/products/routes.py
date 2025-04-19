from flask import Blueprint

products_bp = Blueprint('products', __name__)


@products_bp.route('/products', methods=['GET'])
def get_products():
    return {"message": "List of products"}
