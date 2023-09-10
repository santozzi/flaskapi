from flask import Blueprint, request
from src.services.product_services import *

products = Blueprint('products', __name__)



@products.route("/")
def index():
    return "hola"

# no hace falta methods con get por que es get por defecto
@products.route("/products", methods=['GET'])
def get_products():
    return find_all()

@products.route("/products/<int:product_id>", methods=['GET'])
def get_product(product_id):
    return find_by_id(product_id)

@products.route("/products/", methods=['POST'])
def add_product():
    product = request.json
    return add(product)

@products.route("/products/<int:product_id>", methods=['PUT'])
def update_product(product_id):
    product = request.json
    return update(product,product_id)

@products.route("/products/<int:product_id>", methods=['DELETE'])
def delete_product(product_id):
    return delete(product_id)