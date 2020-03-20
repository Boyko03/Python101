import unittest
from polynomials import Polynomial
from utls import Utls, Term

class TestPolynomials(unittest.TestCase):
	def test_for_making_polynomial_function(self):
		pol = Polynomial('2*x^3+x')

		self.assertEqual(str(pol), '2*x^3+x')

	def test_get_derivative_when_x_has_st_1(self):
		pol = Polynomial('2*x^3+x')

		der = pol.get_derivative()

		self.assertEqual(der, '6*x^2 + 1')

	def test_get_derivative_when_koef_equals_1_and_st_is_diff_than_1(self):
		pol = Polynomial('x^4+10*x^3')

		der = pol.get_derivative()

		self.assertEqual(der, '4*x^3 + 30*x^2')

	def test_get_derivative_when_polynomial_function_is_number_only(self):
		pol = Polynomial('1')

		der = pol.get_derivative()

		self.assertEqual(der, 0)

	def test_get_derivative_when_derivative_power_must_be_1_and_without_star(self):
		pol = Polynomial('3x^2')

		der = pol.get_derivative()

		self.assertEqual(der, '6*x')

if __name__ == '__main__':
	unittest.main()