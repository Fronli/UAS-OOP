import sys
sys.path.append("../repos")
from inventory import global_inventory
# repos.product_repo import getProductPrice
# interaksi ke database
from repos.transaction_repo import save_transaction, get_transaction

# import transacton item
from transaction_item import TransactionItem

# buat class transaction
class Transaction:
    def __init__(self, username):
        self.username = username
        self.items = []
        self.total_price = 0
    
    # menambahkan item ke transaksi 
    def add_item(self, product_obj, qty):
        item = TransactionItem(product_obj, qty)
        self.items.append(item)

    # menyelesaikan transaksi
    def final_transaction(self):
        self.total_price = 0
        for item in self.items:
            self.total_price += item.calculate_subtotal()

        # kurangi stok di inventory
        for item in self.items:
            global_inventory.reduceStock(item.product.id, item.qty)

        # simpan transaksi ke database
        save_transaction(self.username, self.total_price)

# Ambil Semua Transaksi User
def getUserTransaction(username):
    db_list = get_transaction(username)
    return db_list
    
