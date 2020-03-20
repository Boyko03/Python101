from math import gcd

class Fraction:
	def __init__(self, nom, denom):
		if denom == 0:
			raise ValueError('Denominator can not be 0.')
		self.nom = nom
		self.denom = denom

	def __repr__(self):
		return f'({self.nom}, {self.denom})'

	def __str__(self):
		return f'{self.nom}/{self.denom}'

	def __eq__(self, other):
		self.simplify()
		other.simplify()
		return True if self.nom == other.nom and self.denom == other.denom else False

	def __add__(self, other):
		n = (self.nom * other.denom) + (other.nom * self.denom)
		d = self.denom * other.denom

		f = Fraction(n, d)
		f.simplify()
		return f

	def __lt__(self, other):
		self.simplify()
		other.simplify()
		d = self.denom * other.denom

		return True if self.nom * d < other.nom * d else False

	def __le__(self, other):
		self.simplify()
		other.simplify()
		d = self.denom * other.denom

		return True if self.nom * d <= other.nom * d else False

	def __gt__(self, other):
		self.simplify()
		other.simplify()
		d = self.denom * other.denom

		return True if self.nom * d > other.nom * d else False

	def __ge__(self, other):
		self.simplify()
		other.simplify()
		d = self.denom * other.denom

		return True if self.nom * d >= other.nom * d else False


	def simplify(self):
		divider = gcd(self.nom, self.denom)
		self.nom, self.denom = self.nom // divider, self.denom // divider


if __name__ == '__main__':
	main()