from product import Product

class ElectronicProduct(Product):
    # inisiasi constructor product dengan 5 parameter : 
    # id, name, price, category, brand
    def __init__(self, id, name, price, category, brand, warranty_months):
        # panggil constructor Product (parent)
        super().__init__(id, name, price, category, brand)
        # atribut tambahan > garansi bulanan
        self.warranty_months = warranty_months

    # method untuk menampilkan info produk elektronik
    # method yang di override dari class parent (Product)
    def get_info(self):
        return f"[Elektronik] {self.name} | Brand: {self.brand} | Garansi: {self.warranty_months} Bulan"