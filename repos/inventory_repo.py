import sys
sys.path.append("data/")
from data.db_util import query, query_select

def repo_getStock(id):
    result = query_select(f"SELECT * from products where id = {id}")
    return result

def repo_addStock(id, quantity):
    query(f"UPDATE products SET quantity = quantity + {quantity} WHERE id = {id}")

def repo_reduceStock(id, quantity):
    query(f"UPDATE products SET quantity = quantity - {quantity} WHERE id = {id}")

# print(repo_getStock(1))