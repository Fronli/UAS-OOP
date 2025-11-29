import sys
sys.path.append('repos/')
sys.path.append('util/')
from repos.inventory_repo import repo_getStock, repo_reduceStock
from util.exception_h import InsufficientStockErrorH

class Inventory:
    def checkStock(self, id, qty):
        db_list = repo_getStock(id)
        if not db_list:
            return False
        current_qty = db_list[0][6] 
        return current_qty >= qty
        
    def reduceStock(self, id, qty):
        if self.checkStock(id, qty):
            repo_reduceStock(id, qty)        
        else:
            raise InsufficientStockErrorH(f"Stok untuk produk ID {id} tidak cukp!")


global_inventory = Inventory()