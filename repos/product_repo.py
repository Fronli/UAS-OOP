import sys
sys.path.append("data/")
from db_util import query_select

def getProductPrice(id):
    db_list = query_select(f"SELECT * FROM products WHERE id = {id}")
    db_list = db_list[0]
    return db_list[4]

def getAllProduct():
    db_list = query_select(f"SELECT * FROM products ORDER BY id ASC")
    return db_list