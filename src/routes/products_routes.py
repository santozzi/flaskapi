from flask import Blueprint, request
from src.services.products_services import *
#Blue print
products = Blueprint('products', __name__)

@products.route("", methods=['GET'])
def get_products():
    return find_all()

@products.route("/<int:product_id>", methods=['GET'])
def get_product(product_id):
    return find_by_id(product_id)

@products.route("/", methods=['POST'])
def add_product():
    product = request.json
    return add(product)

@products.route("/<int:product_id>", methods=['PUT'])
def update_product(product_id):
    product = request.json
    return update(product,product_id)

@products.route("/<int:product_id>", methods=['DELETE'])
def delete_product(product_id):
    return delete(product_id)

@products.route("/<int:product_id>", methods=['POST'])
def add_new_image(product_id:int):
    image = request.json
    return add_image(image,product_id)

@products.route("/<int:product_id>/<int:image_pos>", methods=['DELETE'])
def delete_image_product(product_id:int,image_pos:int):
    return delete_image(image_pos,product_id)