from src.models.local.products_model import *

                              
def init():
    init_model()
    
def find_all():
    return find_all_model()

def find_by_id(id:int):
    return find_by_id_model(id)

def add(product):
    return add_model(product)

def update(producto,id):
    return update_model(producto,id)

def delete(id):
    return delete_model(id)