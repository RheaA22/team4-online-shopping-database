from flask import Flask
from api.backend.products.routes import products_bp
from api.backend.categories.routes import categories_bp
from api.backend.users.routes import users_bp
from api.backend.orders import orders_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(products_bp, url_prefix='/api')
    app.register_blueprint(categories_bp, url_prefix='/api')
    app.register_blueprint(users_bp, url_prefix='/api')
    app.register_blueprint(orders_bp, url_prefix='/api')
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=4000)
