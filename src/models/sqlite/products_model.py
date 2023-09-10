# from flask import Blueprint, request
# from model.sqlite.connection import get_db
# from model.sqlite.entities.product import Product
# sqlite_products = Blueprint('sqlite_products', __name__)

# db = get_db()


# @sqlite_products.route('/sqlite/products', methods=['POST'])
# def add_model(product):
#     producto = Product(product['name'], product['price'], product['quantity'])
#     db.session.add(producto)

#     return product