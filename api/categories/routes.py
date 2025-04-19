from flask import Blueprint

categories_bp = Blueprint('categories', __name__)


@categories_bp.route('/categories', methods=['GET'])
def get_categories():
    return {"message": "List of categories"}
