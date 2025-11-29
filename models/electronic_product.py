from product import Product

class ElectronicProduct(Product):
    def __init__(self, id, name, price, category, brand, warranty_month):
        super().__init__(id, name, price, category, brand)
        self.warranty_month = warranty_month