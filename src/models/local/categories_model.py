from flask import jsonify

categories= list()
categories_default= [
    {"id":0,"name": "Soldadoras"},
    {"id":1,"name": "Smartphones"},
    {"id":2,"name": "Tablets"},
    {"id":3,"name": "Laptops"},
    {"id":4,"name": "Cámaras"},
    {"id":5,"name": "Accesorios"},
    {"id":6,"name": "Televisores"},
    {"id":7,"name": "Consolas"},
    {"id":8,"name": "Altavoces"},
    {"id":9,"name": "Routers"},
    {"id":10,"name": "Impresoras"},
]
#TODO que pasa cuendo borro una categoria que esta usada en un producto

def init_model():
    """
    Inicializa el modelo con las categorías de la lista categories_default
    """
    for item in categories_default:
        categories.append(item)

def find_all_model():
    """
    Devuelve todos las categorias
    """

    return categories

def find_by_id_model(id:int):
    """
    Devuelve una categoría por id
    """
    
    category = [category for category in categories if category['id'] == id]

    
    if len(category) == 0:
        return {'message': 'category not found'}
    
    return category[0]

def add_model(category):
   """
   Agrega una categoría a la lista de categorías
   """

   if len(categories) == 0:
         category["id"] = 0
   else:
        
         category["id"] = categories[-1]["id"] + 1
   categories.append(category)

   return category

def update_model(categoria,id):
    """
    Actualiza cateogria por id
    """
    category = [category for category in categories if category['id'] == id]
    if len(category) == 0:
        return jsonify({'message': 'Category not found'})
    category[0]['name'] = categoria['name']
 
    
    return category

def delete_model(id):
    """
    Elimina una categoría por id
    """
    category = [category for category in categories if category['id'] == id]
    if len(category) == 0:
        return jsonify({'message': 'Product not found'})
    categories.remove(category[0])
    return category[0]