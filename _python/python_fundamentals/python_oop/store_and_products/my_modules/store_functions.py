def print_products(self):
  for product in self.products:
    print(product.name)

def add_product(self, new_product):
  self.products.append(new_product)
  return self

def sell_product(self, id):
  self.products.pop(id)
  return self

def inflation(self, percent_increase):
  for product in self.products:
    product.price += percent_increase
    print(f"{product.name}s price increased to {product.price}")

def set_clearance(self, category, percent_discount):
  for product in self.products:
    if product.category == category:
      product.price -= percent_discount
      print(f"{product.name}s price decreased to {product.price}")
