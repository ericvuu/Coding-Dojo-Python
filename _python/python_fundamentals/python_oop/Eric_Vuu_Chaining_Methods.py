class User:
    def __init__(self, name, email):
      self.name = name
      self.email = email
      self.account_balance = 0

    def make_deposit(self, amount):
      self.account_balance += amount
      return self

    def make_withdrawal(self, amount):
      self.account_balance -= amount
      return self

    def transfer_money(self, other_user, amount):
      self.account_balance -= amount
      other_user.account_balance += amount
      return self

    def display_user_balance(self):
      print(f"User: {self.name}, balance: ${self.account_balance}")



user1 = User("John Doe", "john@gmail.com")
user2 = User("Jane Doe", "jane@gmail.com")
user3 = User("Lebron James", "lebron@lakers.com")


user1.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(1000).display_user_balance()
user2.make_deposit(10000).make_deposit(1000).make_withdrawal(2000).display_user_balance()
user3.make_deposit(5000000).make_withdrawal(10000).make_withdrawal(10000).make_withdrawal(10000).display_user_balance()

user1.transfer_money(user3, 100).display_user_balance()
user3.display_user_balance()
