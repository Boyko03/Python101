import unittest
from polynomials import Polynomial
from utls import Utls, Term

class TestUtls(unittest.TestCase):
	def test_to_terms_function(self):
		pol = Polynomial('2*x+1')

		result = pol.to_terms()

		expected = [Term('2*x'), Term('1')]
		self.assertEqual(result, expected)

class TestTerm(unittest.TestCase):
	#get_term_derivative() returns a list
	def test_get_term_derivative_when_term_is_only_x(self):
		term = Term('x')

		result = term.get_term_derivative()

		expected = ['1']
		self.assertEqual(result, expected)

	def test_get_term_derivative_when_term_has_koef(self):
		term = Term('5*x')

		result = term.get_term_derivative()

		expected = ['5']
		self.assertEqual(result, expected)

	def test_get_term_derivative_when_term_has_st(self):
		term = Term('x^5')

		result = term.get_term_derivative()

		expected = ['5*x^4']
		self.assertEqual(result, expected)

	def test_get_term_derivative_when_term_has_koef_and_st(self):
		term = Term('5*x^3')

		result = term.get_term_derivative()

		expected = ['15*x^2']
		self.assertEqual(result, expected)

	def test_get_term_derivative_when_term_has_koef_and_st_but_koef_is_without_operator(self):
		term = Term('5x^2')

		result = term.get_term_derivative()

		expected = ['10*x']
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()