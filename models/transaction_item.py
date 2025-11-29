from product import Product

class TransactionItem:
    def __init__(self, product : Product, qty : int):
        self.product = product
        self.qty = qty

    def calculate_subtotal(self):
        return self.product.price * self.qty