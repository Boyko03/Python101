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

		return int(c), int(n)

	def __str__(self):
		return self.term

	def __repr__(self):
		return self.term

	def __eq__(self, other):
		return self.term == other.term

	def get_term_derivative(self):
		c = self.c
		n = self.n

		if c == 1:
			if n == 1:
				return ['1']
			elif n == 2:
				return ['x']
			else:
				return [f'{n}*x^{n - 1}']
		else:
			if n == 1:
				return [f'{c * n}']
			elif n == 2:
				return [f'{c * n}*x']
			else:
				return [f'{c * n}*x^{n - 1}']

class Utls(Term):
	def __str__(self):
		return f'{self.pol}'

	def to_terms(self):
		terms = self.pol.split('+')
		return [Term(term) for term in terms]

	def modify_pol(self):
		pol = self.pol
		pol = pol.split('+')
		self.pol = ' + '.join(pol)

if __name__ == '__main__':
	main()