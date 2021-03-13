class BankAccount:
  def __init__(self, int_Rate=0.01, balance=0):
    self.int_Rate = int_Rate
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if self.balance > 0:
      self.balance -= amount
      return self
    else:
      self.balance -= 5
      print(f"Insufficient funds: Charging a $5 fee")
      return self

  def display_account_info(self):
      print(f"Balance: ${self.balance}")

  def yield_interest(self):
    if self.balance > 0:
      self.balance += self.balance * self.int_Rate
      return self
    else:
      return self

account1 = BankAccount()
account2 = BankAccount()
account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
