class Term:
	def __init__(self, term):
		self.term = term
		self.c, self.n = Term.parse(term)

	@staticmethod
	def parse(string):
		c = 1
		n = 1
		if '*' in string:
			c = string.split('*')[0]
		else:
			if string.split('x')[0] == '':
				c = 1
			else:
				c = string.split('x')[0]

		if '^' in string:
			n = string.split('^')[1]

		return c, n

	def __str__(self):
		return self.term

	def __eq__(self, other):
		return self.term == other.term

	def get_term_derivative(self):
		c = self.c
		n = self.n

		if c == 1:
			if n == 1:
				return 1
			else:
				return [f'x{f'^{n - 1}' if n != 2 else 1}']
		else:
			if n == 1:
				return [f'{c * n}']
			else:
				return [f'{c * n}*x{f'^{n - 1}' if n != 2 else '1'}']

class Utls(Term):
	def __str__(self):
		return f'{self.pol}'

	def to_terms(self):
		terms = self.pol.split('+')
		return [Term(term) for term in terms]

if __name__ == '__main__':
	main()