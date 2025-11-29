class InsufficientStockErrorH(Exception):
    """Stock tidak mencukupi!"""
    pass

class NegativePrice(Exception):
    """Ngasih harga gk boleh negatif!"""

class FailedAddingProduct(Exception):
    """Gagal nambahin product!"""

class FailedChangingPrice(Exception):
    """Gagal merubah harga product!"""

class FailedAddingQuantity(Exception):
    """Gagal menambahkan quantity product!"""