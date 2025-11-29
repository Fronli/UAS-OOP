import sys
from inventory import global_inventory

sys.path.append("../repos")
from product_repo import getProductPrice
from transaction_repo import save_transaction, get_transaction

class Transaction:
    def __init__(self, product_list, username):
        self.product_list = product_list
        self.total_price = 0
        self.username = username
    
    def add_item(self):
        for item in self.product_list:
            global_inventory.reduceStock(item["product"], item["qty"])

    def calculate_total(self):
        for item in self.product_list:
            self.total_price += getProductPrice(item["product"]) * item["qty"]

    def final_transaction(self):
        self.add_item()
        self.calculate_total()
        save_transaction(self.username, self.total_price)


def getUserTransaction(username):
    db_list = get_transaction(username)
    return db_list
    
