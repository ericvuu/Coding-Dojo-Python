class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accounts = {
      "checking": BankAccount(int_rate=0.02, balance=0),
      "savings": BankAccount(int_rate=0.02, balance=0),
      "roth_ira": BankAccount(int_rate=0.02, balance=0),
      "ira": BankAccount(int_rate=0.02, balance=0),
    }

  def make_deposit(self, amount, type):
    self.accounts[type].balance += amount
    return self

  def make_withdrawal(self, amount, type):
    self.accounts[type].balance -= amount
    return self

  def transfer_money(self, type, other_user, other_user_type, amount):
    self.accounts[type].balance -= amount
    other_user.accounts[other_user_type].balance += amount
    return self

  def display_user_balance(self, type):
    print(f"User: {self.name}, balance: ${self.accounts[type].balance}")

# Bank Account Object

class BankAccount:
  def __init__(self, int_rate=0.02, balance=0):
    self.int_rate = int_rate
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
      self.balance += self.balance * self.int_rate
      return self
    else:
      return self


user1 = User("John Doe", "john@gmail.com")
user2 = User("Jane Doe", "jane@gmail.com")
user3 = User("Lebron James", "lebron@lakers.com")

user1.make_deposit(1000,"checking").make_deposit(1000,"checking").make_deposit(1000,"checking").make_withdrawal(1000,"checking").transfer_money("checking",user3,"checking",100).display_user_balance("checking")
user2.make_deposit(10000,"savings").make_deposit(1000,"checking").make_withdrawal(2000, "savings").display_user_balance("savings")
user2.display_user_balance("checking")
user3.make_deposit(5000000, "ira").make_deposit(70000000, "checking").make_withdrawal(10000,"checking").make_withdrawal(10000, "checking").make_withdrawal(10000, "checking").display_user_balance("ira")
user3.display_user_balance("checking")
