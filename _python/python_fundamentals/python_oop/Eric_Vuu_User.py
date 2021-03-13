class User:
    def __init__(self, name, email):
      self.name = name
      self.email = email
      self.account_balance = 0

    def make_deposit(self, amount):
      self.account_balance += amount

    def make_withdrawal(self, amount):
      self.account_balance -= amount

    def display_user_balance(self):
      print(f"User: {self.name}, balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
      self.account_balance -= amount
      other_user.account_balance += amount

user1 = User("John Doe", "john@gmail.com")
user2 = User("Jane Doe", "jane@gmail.com")
user3 = User("Lebron James", "lebron@lakers.com")


user1.make_deposit(1000)
user1.make_deposit(1000)
user1.make_deposit(1000)
user1.make_withdrawal(1000)
user1.display_user_balance()

user2.make_deposit(10000)
user2.make_deposit(1000)
user2.make_withdrawal(2000)
user2.display_user_balance()

user3.make_deposit(5000000)
user3.make_withdrawal(10000)
user3.make_withdrawal(10000)
user3.make_withdrawal(10000)
user3.display_user_balance()

user1.transfer_money(user3, 100)
user1.display_user_balance()
user3.display_user_balance()
