from flask import Flask
from src.routes.products_routes import products



app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model/sqlite/db/tasks.db'
#db = SQLAlchemy(app)

def init_app():
    #configuration
    #app.config.from_object(config)

    #blueprints
    app.register_blueprint(products)

    return app