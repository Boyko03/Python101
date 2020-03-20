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
		return f'{self.amount}'

	def __eq__(self, other):
		return True if self.amount == other.amount else False

if __name__ == '__main__':
	main()