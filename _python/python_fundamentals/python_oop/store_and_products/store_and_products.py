from my_modules import store_functions
from my_modules import products_functions

class Store:
  def __init__(self, name, products=[]):
    self.name = name
    self.products = products

class Product:
  def __init__(self, name, price, category):
    self.name = name
    self.price = price
    self.category = category

store1 = Store("Target")
product1 = Product("apple", 1, "fruit")
product2 = Product("Beer", 6, "alcohol")
product3 = Product("legos", 40, "toys")
product4 = Product("banana", 1, "fruit")

store_functions.add_product(store1, product1)
store_functions.add_product(store1, product2)
store_functions.add_product(store1, product3)

store_functions.print_products(store1)
store_functions.set_clearance(store1,"toys", .10)
store_functions.add_product(store1, product4)
