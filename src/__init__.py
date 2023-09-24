from flask import Flask, redirect
from src.routes.products_routes import products
from src.routes.categories_routes import categories

app = Flask(__name__)

URL_PREFIX = '/api/v1'
def init_app():
    #configuration
 

    #redireccion a documentación
    @app.route("/")
    def go_to_documentation():
     return redirect('/api/docs')

    #blueprints

    app.register_blueprint(products, url_prefix=URL_PREFIX+'/products/')
    app.register_blueprint(categories, url_prefix=URL_PREFIX+'/categories/')

    return app