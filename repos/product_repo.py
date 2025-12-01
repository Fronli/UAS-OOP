import sys
sys.path.append("data/")
# tambahkan folder 'data/' ke path agar db_util bisa di-import
from data.db_util import query, query_select
# query        → eksekusi SQL (INSERT, UPDATE, DELETE)
# query_select → eksekusi SELECT dan mengembalikan data (list of tuple)


def getProductInfo(id):
    # mengambil 1 produk berdasarkan ID
    db_list = query_select(f"SELECT * FROM products WHERE id = {id}")
    db_list = db_list[0]    # ambil record pertama (database mengembalikan list)
    return db_list          # return data produk

def getAllProduct():
    # mengambil seluruh produk yang ada di tabel products
    db_list = query_select(f"SELECT * FROM products ORDER BY id ASC")
    return db_list          # return list of produk

def addProduct(p):
    # menambahkan produk baru ke database
    # isi > name, category, brand, price, warranty_months, quantity default = 0
    query(f"INSERT INTO products (name, category, brand, price, warranty_months, quantity) VALUES ('{p.name}', '{p.category}', '{p.brand}', {p.price}, {p.warranty_months}, 0)")

def changePrice(id, new_price):
    # mengubah harga produk berdasarkan ID
    query(f"UPDATE products SET price = {new_price} WHERE id = {id}")