from flask import Blueprint, request
from src.services.categories_services import *
#Blue print
categories = Blueprint('categories', __name__)

@categories.route("", methods=['GET'])
def get_categories():
    return find_all()

@categories.route("/<int:category_id>", methods=['GET'])
def get_category(category_id):
    return find_by_id(category_id)

@categories.route("/", methods=['POST'])
def add_category():
    category = request.json
    return add(category)

@categories.route("/<int:category_id>", methods=['PUT'])
def update_categoryt(category_id):
    category = request.json
    return update(category,category_id)

@categories.route("/<int:category_id>", methods=['DELETE'])
def delete_category(category_id):
    return delete(category_id)

