from src import init_app
from flask_swagger_ui import get_swaggerui_blueprint
from src.services.products_services import init
from src.models.local.categories_model import init_model as init_categories_model
from flask_cors import CORS

app = init_app()
#se pueda acceder desde cualquier origen
CORS(app)
#swagger
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Proyecto Programación II - UTN"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)



if __name__ == "__main__":
    
    init()
    init_categories_model()
    app.run(debug=True, port=4000)