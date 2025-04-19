from flask import Flask
from .products.routes import products_bp
from .categories.routes import categories_bp
from .users.routes import users_bp
from .orders.routes import orders_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(products_bp, url_prefix='/api')
    app.register_blueprint(categories_bp, url_prefix='/api')
    app.register_blueprint(users_bp, url_prefix='/api')
    app.register_blueprint(orders_bp, url_prefix='/api')
    return app
