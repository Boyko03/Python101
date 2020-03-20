import unittest
from polynomials import Polynomial
from utls import Utls, Term

class TestPolynomials(unittest.TestCase):
	def test_for_making_polynomial_function(self):
		pol = Polynomial('2*x^3+x')

		self.assertEqual(str(pol), '2*x^3+x')

if __name__ == '__main__':
	unittest.main()