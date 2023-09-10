
from flask import jsonify


products = list();
products_technology = [
    {"id":1,"name": "Smartphone X", "price": 599.99, "quantity": 50},
    {"id":2,"name": "Tablet Pro", "price": 349.99, "quantity": 30},
    {"id":3,"name": "Laptop Ultra", "price": 999.99, "quantity": 20},
    {"id":4,"name": "Cámara Digital 4K", "price": 449.99, "quantity": 40},
    {"id":5,"name": "Auriculares Inalámbricos", "price": 89.99, "quantity": 100},
    {"id":6,"name": "Smart TV 55 pulgadas", "price": 799.99, "quantity": 15},
    {"id":7,"name": "Consola de Juegos Pro", "price": 399.99, "quantity": 25},
    {"id":8,"name": "Altavoz Bluetooth Premium", "price": 149.99, "quantity": 60},
    {"id":9,"name": "Router Wi-Fi de Alta Velocidad", "price": 79.99, "quantity": 35},
    {"id":10,"name": "Impresora Multifunción", "price": 199.99, "quantity": 10},
]
def init_model():
    for item in products_technology:
        products.append(item)

def find_all_model():
    return products

def find_by_id_model(id:int):
    product = [product for product in products if product['id'] == id]
    if len(product) == 0:
        return jsonify({'message': 'Product not found'})
    return product[0]

def add_model(product):
   
   if len(products) == 0:
         product["id"] = 0
   else:
         print (product)
         product["id"] = products[-1]["id"] + 1


   products.append(product)

   return product

def update_model(producto,id):
    product = [product for product in products if product['id'] == id]
    if len(product) == 0:
        return jsonify({'message': 'Product not found'})
    product[0]['name'] = producto['name']
    product[0]['price'] = producto['price']
    product[0]['quantity'] = producto['quantity']
    return product[0]

def delete_model(id):
    product = [product for product in products if product['id'] == id]
    if len(product) == 0:
        return jsonify({'message': 'Product not found'})
    products.remove(product[0])
    return jsonify({'message': 'Product deleted'})