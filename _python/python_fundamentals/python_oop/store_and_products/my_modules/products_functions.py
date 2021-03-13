def update_price(self, percent_change, is_increased):
  if is_increased == True:
    self.price += percent_change
  else:
    self.price -= percent_change
  return self

def print_info(self):
  print(f"The name of the product is {self.name}.\nThe price is ${self.price}.\nThe category is {self.category}.")
