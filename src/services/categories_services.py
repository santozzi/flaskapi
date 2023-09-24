from src.models.local.categories_model import *

                              
def init():
    init_model()
    
def find_all():
    return find_all_model()

def find_by_id(id:int):
    return find_by_id_model(id)

def add(category):
    return add_model(category)

def update(category,id):
    return update_model(category,id)

def delete(id):
    return delete_model(id)