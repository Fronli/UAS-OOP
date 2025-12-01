import unittest
import sys
# tambahkan folder models/ agar bisa import model class
sys.path.append('models/')

from models.electronic_product import ElectronicProduct
from models.transaction_item import TransactionItem

class TestTransactionLogic(unittest.TestCase):
    
    def setUp(self):
        # dummy data
        self.laptop = ElectronicProduct(11, "Laptop Gaming", 100, "Laptop", "Asus", 24)
    
    def test_product_encapsulation(self):
        # buat ngetest kalo ngasih harg anegatif
        with self.assertRaises(ValueError):
            self.laptop.price = -5000

    def test_transaction_item_subtotal(self):
        # buat ngetest fitur hitung harga
        qty = 2
        item = TransactionItem(self.laptop, qty)
        expected_total = 200
        self.assertEqual(item.calculate_subtotal(), expected_total)

if __name__ == '__main__':
    unittest.main()