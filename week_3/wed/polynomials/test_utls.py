import unittest
from polynomials import Polynomial
from utls import Utls, Term

class TestUtls(unittest.TestCase):
	def test_to_terms_function(self):
		pol = Polynomial('2*x+1')

		result = pol.to_terms()

		expected = [Term('2*x'), Term('1')]
		self.assertEqual(result, expected)

	def test_get_derivative(self):
		pol = Polynomial('2*x^3+x')

		der = pol.get_derivative()

		self.assertEqual(der, '6*x^2 + 1')

	# def test_get_derivative_2(self):
	# 	pol = Polynomial('x^4+10*x^3')

	# 	der = pol.get_derivative()

	# 	self.assertEqual(der, '4*x^3 + 30*x^2')

	# def test_when_polynomial_function_is_number_only(self):
	# 	pol = Polynomial('1')

	# 	der = pol.get_derivative()

	# 	self.assertEqual(der, 0)

	# def test_when_derivative_power_must_be_1_and_without_star(self):
	# 	pol = Polynomial('3x^2')

	# 	der = pol.get_derivative()

	# 	self.assertEqual(der, '6*x')

if __name__ == '__main__':
	unittest.main()