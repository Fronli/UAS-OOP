import sys
sys.path.append('util/')
from abc import ABC, abstractmethod
from util.exception_h import NegativePrice

class Product(ABC): 
    def __init__(self, id, name, price, category, brand):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.brand = brand

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise NegativePrice("Harga tidak boleh negatif!")
        self.__price = value
    
    @abstractmethod
    def get_info():
        pass
