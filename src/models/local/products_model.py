from flask import jsonify
from src.models.local.categories_model import find_by_id_model as find_category_by_id_model


# Lista de productos
categories = list();

products_technology = [
    {"id":1,"name": "Smartphone X", "price": 599.99, "quantity": 50, "category": 3 , "photoUrls": ["https://picsum.photos/200/300"]},
    {"id":2,"name": "Tablet Pro", "price": 349.99, "quantity": 30 , "category": 2, "photoUrls": ["https://picsum.photos/200/300"] },
    {"id":3,"name": "Laptop Ultra", "price": 999.99, "quantity": 20 , "category": 3, "photoUrls": ["https://picsum.photos/200/300"]},
    {"id":4,"name": "Cámara Digital 4K", "price": 449.99, "quantity": 40 , "category":1, "photoUrls": ["https://picsum.photos/200/300"]},
    {"id":5,"name": "Auriculares Inalámbricos", "price": 89.99, "quantity": 100 , "category": 2, "photoUrls": ["https://picsum.photos/200/300"]} ,
    {"id":6,"name": "Smart TV 55 pulgadas", "price": 799.99, "quantity": 15 , "category": 1, "photoUrls": ["https://picsum.photos/200/300"]},
    {"id":7,"name": "Consola de Juegos Pro", "price": 399.99, "quantity": 25 , "category": 0, "photoUrls": ["https://picsum.photos/200/300"]},
    {"id":8,"name": "Altavoz Bluetooth Premium", "price": 149.99, "quantity": 60 , "category": 3, "photoUrls": ["https://picsum.photos/200/300"]},
    {"id":9,"name": "Router Wi-Fi de Alta Velocidad", "price": 79.99, "quantity": 35 , "category": 2, "photoUrls": ["https://picsum.photos/200/300"]},
    {"id":10,"name": "Impresora Multifunción", "price": 199.99, "quantity": 10 , "category": 1, "photoUrls": ["https://picsum.photos/200/300"]},
]

def init_model():
    """
    Inicializa el modelo con los productos de la lista products_technology
    """
    for item in products_technology:
        categories.append(item)
def clone(product):
    producto = dict()
    producto["id"]=product["id"]
    producto["name"]=product["name"]
    producto["price"]=product["price"]
    producto["quantity"]=product["quantity"]
    producto["photoUrls"]=product["photoUrls"]
    producto["category"]=product["category"]
    return producto

def find_all_model():
    """
    Devuelve todos los productos
    """
    lista = list()
    producto = {}
    for item in categories:
        producto = clone(item)
        producto["category"] = find_category_by_id_model(producto["category"])
        lista.append(producto)

    return lista


def find_by_id_model(id:int):
    """
    Devuelve un producto por id
    """
    producto = dict()
    product = [product for product in categories if product['id'] == id]
   
    if len(product) == 0:
        return jsonify({'message': 'Product not found'})
    else:
        producto = clone(product[0])


        producto["category"] = find_category_by_id_model(product[0]["category"])
    return producto

def add_model(product):
   """
   Agrega un producto a la lista de productos
   """

   if len(categories) == 0:
         product["id"] = 0
   else:
         print (product)
         product["id"] = categories[-1]["id"] + 1
   categories.append(product)

   return find_by_id_model(product["id"])

def update_model(producto,id):
    """
    Actualiza un producto por id
    """
    product = [product for product in categories if product['id'] == id]
    if len(product) == 0:
        return jsonify({'message': 'Product not found'})
    product[0]['name'] = producto['name']
    product[0]['price'] = producto['price']
    product[0]['quantity'] = producto['quantity']
    product[0]['category'] = producto['category']
    product[0]['photoUrls'] = producto['photoUrls']   
    
    return find_by_id_model(id)

def delete_model(id):
    """
    Elimina un producto por id
    """
    product = [product for product in categories if product['id'] == id]
    if len(product) == 0:
        return jsonify({'message': 'Product not found'})
    categories.remove(product[0])
    return jsonify({'message': 'Product deleted'})

def add_image_model(image,product_id:int):
    """
    Agrega una imagen a un producto
    """
    product = [product for product in categories if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'message': 'Product not found'})
    product[0]['photoUrls'].append(image['url'])
    return find_by_id_model(product_id)

def delete_image_model(image_pos:int,product_id:int):
    """
    Elimina una imagen de un producto
    """
    product = [product for product in categories if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'message': 'Product not found'})
    lista_images = product[0]['photoUrls']
    if len(lista_images) > 0:
        print (f"Esta es una lista de imagenes {lista_images}")
        lista_images.remove(lista_images[image_pos])
        print (f"Esta es una lista de imagenes {lista_images}")
    return find_by_id_model(product_id)