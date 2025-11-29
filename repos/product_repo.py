import sys
sys.path.append("data/")
from data.db_util import query_select

def getProductInfo(id):
    db_list = query_select(f"SELECT * FROM products WHERE id = {id}")
    db_list = db_list[0]
    return db_list

def getAllProduct():
    db_list = query_select(f"SELECT * FROM products ORDER BY id ASC")
    return db_list