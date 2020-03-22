class Bill:
	def __init__(self, amount):
		if type(amount) != int:
			raise TypeError('Invalid type.')
		if amount < 0:
			raise ValueError('Invalid value.')
		self.amount = amount

	def __int__(self):
		return self.amount

	def __str__(self):
		return f'A {self.amount}$ bill'

	def __repr__(self):
		return f'A {self.amount}$ bill'

	def __eq__(self, other):
		return True if self.amount == other.amount else False

	def __hash__(self):
		return hash(self.amount)

class BillBatch:
	def __init__(self, bills):
		self.bills = bills

	def __len__(self):
		return len(self.bills)

	def total(self):
		total = 0
		for bill in self.bills:
			total += int(bill)

		return total

	def __getitem__(self, index):
		return self.bills[index]

class CashDesk:
	def __init__(self):
		self.money_holder = {}

	def take_money(self, money):
		if type(money) == Bill:
			if money in self.money_holder:
				self.money_holder[money] += 1
			else:
				self.money_holder[money] = 1
			return

		for bill in money:
			if bill in self.money_holder:
				self.money_holder[bill] += 1
			else:
				self.money_holder[bill] = 1

	def total(self):
		t = 0
		for bill in self.money_holder:
			t += int(bill) * self.money_holder[bill]

		return t

	def inspect(self):
		for bill in self.money_holder:
			print(f'{int(bill)}$ bills - {self.money_holder[bill]}')

if __name__ == '__main__':
	main()