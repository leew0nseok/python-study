
class BankAccount:
	def __init__(self, acc_name=None, acc_number=None, balance=0):
		self.account_name = acc_name
		self.account_number = acc_number
		self.balance = balance
	
	def show_balance(self):
		print(self.balance)
	
	def show_account_info(self):
		print(self.account_number, self.account_name, self.balance)
	
	def deposit(self, amount):
		self.balance += amount
	
	def withdraw(self, amount):
		self.balance -= amount


acc = BankAccount("Mr. Kim", 10476, 30000)
acc.show_balance()
acc.deposit(20000)
acc.show_balance()
acc.withdraw(10000)
acc.show_balance()