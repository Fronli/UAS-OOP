import sys
sys.path.append("data/")
# tambahkan folder 'data/' ke path agar modul db_util bisa ditemukan
from data.db_util import query, query_select
# query > eksekusi SQL tanpa return (INSERT, UPDATE, DELETE)
# query_select > eksekusi SQL SELECT dan mengembalikan hasil query sebagai list data


def save_transaction(customer_name, total_amount):
    # menyimpan transaksi baru ke tabel 'transactions'
    # parameter:
    #   customer_name > nama pembeli
    #   total_amount  > total harga semua item
    query(f"INSERT INTO transactions (customer_name, total_amount) VALUES ('{customer_name}', {total_amount})")

def get_transaction(customer_name):
    # mengambil semua transaksi milik customer tertentu
    db_list = query_select(f"SELECT * FROM transactions WHERE customer_name = '{customer_name}'")
    return db_list   # return list of transaksi