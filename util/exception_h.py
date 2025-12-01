# exception khusus ketika stok barang tidak cukup saat transaksi/restock/checkout
class InsufficientStockErrorH(Exception):
    """Stock tidak mencukupi!"""
    pass

# exception untuk mencegah harga negatif pada produk
class NegativePrice(Exception):
    """Ngasih harga gk boleh negatif!"""
    pass

# exception saat penambahan produk ke database gagal (misal: SQL error)
class FailedAddingProduct(Exception):
    """Gagal nambahin product!"""
    pass

# exception saat perubahan harga produk gagal (misal: ID tidak ditemukan)
class FailedChangingPrice(Exception):
    """Gagal merubah harga product!"""
    pass

# exception jika gagal menambah quantity stok (misal: DB error)
class FailedAddingQuantity(Exception):
    """Gagal menambahkan quantity product!"""
    pass