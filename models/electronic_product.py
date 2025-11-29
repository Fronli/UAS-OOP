from product import Product

class ElectronicProduct(Product):
    def __init__(self, id, name, price, category, brand, warranty_months):
        super().__init__(id, name, price, category, brand)
        self.warranty_months = warranty_months

    def get_info(self):
        return f"[Elektronik] {self.name} | Brand: {self.brand} | Garansi: {self.warranty_months} Bulan"