# import product
from product import Product

# buat class Transaction
class TransactionItem:
    def __init__(self, product : Product, qty : int):
        self.product = product  # object product-nya
        self.qty = qty          # jumlah qty yang dibeli

    def calculate_subtotal(self):
        # logic untuk menghitung subtotal
        return self.product.price * self.qty