import sys
sys.path.append("data/")
from data.db_util import query, query_select

def getProductInfo(id):
    db_list = query_select(f"SELECT * FROM products WHERE id = {id}")
    db_list = db_list[0]
    return db_list

def getAllProduct():
    db_list = query_select(f"SELECT * FROM products ORDER BY id ASC")
    return db_list

def addProduct(p):
    query(f"INSERT INTO products (name, category, brand, price, warranty_months, quantity) VALUES ({p.name}, {p.category}, {p.brand}, {p.price}, {p.warranty_months}, 0)")

def changePrice(id, new_price):
    query(f"UPDATE products SET price = {new_price} WHERE id = {id}")