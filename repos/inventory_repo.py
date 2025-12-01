import sys
sys.path.append("data/")

from data.db_util import query, query_select
# query         → eksekusi perintah SQL (INSERT/UPDATE/DELETE)
# query_select  → eksekusi SQL SELECT dan mengembalikan hasilnya


def repo_getStock(id):
    # mengambil data produk berdasarkan ID dari tabel 'products'
    result = query_select(f"SELECT * from products where id = {id}")
    return result

def repo_addStock(id, quantity):
    # menambahkan stok produk dengan menambah kolom quantity
    query(f"UPDATE products SET quantity = quantity + {quantity} WHERE id = {id}")

def repo_reduceStock(id, quantity):
    # mengurangi stok produk sesuai jumlah yang dibeli
    query(f"UPDATE products SET quantity = quantity - {quantity} WHERE id = {id}")

# contoh debugging untuk melihat data produk ID 1
# print(repo_getStock(1))