import sys
sys.path.append('repos/')
from inventory_repo import repo_getStock, repo_addStock, repo_reduceStock

class Inventory:
    def checkStock(self, id, qty):
        db_list = repo_getStock(id)
        db_list = db_list[0]
        if db_list[6] - qty >= 0:
            return True
        else: 
            return False
        
    def addStock(self, id, qty):
        repo_addStock(id, qty)

    def reduceStock(self, id, qty):
        check_flag = self.checkStock(id, qty)
        if check_flag:
            repo_reduceStock(id, qty)        
        else:
            print("Insufficient stock!")


global_inventory = Inventory()

# print(inv.checkStock(1, 16))