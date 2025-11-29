import sys
sys.path.append("../repos")
from inventory import global_inventory
# from repos.product_repo import getProductPrice
from repos.transaction_repo import save_transaction, get_transaction
from transaction_item import TransactionItem

class Transaction:
    def __init__(self, username):
        self.username = username
        self.items = []
        self.total_price = 0
    
    def add_item(self, product_obj, qty):
        item = TransactionItem(product_obj, qty)
        self.items.append(item)

    def final_transaction(self):
        self.total_price = 0
        for item in self.items:
            self.total_price += item.calculate_subtotal()

        for item in self.items:
            global_inventory.reduceStock(item.product.id, item.qty)

        save_transaction(self.username, self.total_price)


def getUserTransaction(username):
    db_list = get_transaction(username)
    return db_list
    
