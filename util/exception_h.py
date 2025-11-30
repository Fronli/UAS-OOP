class InsufficientStockErrorH(Exception):
    """Stock tidak mencukupi!"""
    pass

class NegativePrice(Exception):
    """Ngasih harga gk boleh negatif!"""
    pass

class FailedAddingProduct(Exception):
    """Gagal nambahin product!"""
    pass

class FailedChangingPrice(Exception):
    """Gagal merubah harga product!"""
    pass

class FailedAddingQuantity(Exception):
    """Gagal menambahkan quantity product!"""
    pass