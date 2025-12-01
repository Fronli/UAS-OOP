# import sys untuk manipulasi path
import sys
sys.path.append('util/')  # tambahkan path util 

# Dipakai untuk bikin kelas abstrak yang tidak boleh diinstansiasi langsung
from abc import ABC, abstractmethod
# import exception handling untuk validasi harga 
from util.exception_h import NegativePrice


class Product(ABC): 
    # inisiasi atribut dasar product
    def __init__(self, id, name, price, category, brand):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.brand = brand

    # Getter 
    @property
    def price(self):
        # mengembalikan nilai harga product 
        return self.__price
    
    # Setter 
    @price.setter
    def price(self, value):
        # check apakah dibawah 0 hargannya
        # kalau tidak valid : (dibawah 0)
        if value < 0:
            raise NegativePrice("Harga tidak boleh negatif!")
        # kalau valid, set harga
        self.__price = value
    
    @abstractmethod
    def get_info():
        pass
