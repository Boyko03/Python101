import unittest
from fractions import Fraction

class TestClassFractions(unittest.TestCase):
	def test_object_init(self):
		nom = 1
		denom = 2

		a = Fraction(1, 2)
		result = (a.nom, a.denom)

		expected = (1, 2)
		self.assertEqual(result, expected)

	def test_simplify_fractions(self):
		fraction = Fraction(2, 4)

		fraction.simplify()

		expected = Fraction(1, 2)
		self.assertEqual(fraction, expected)

	def test_collect_fractions(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(2, 3)

		result = f1 + f2

		expected = Fraction(7, 6)
		self.assertEqual(result, expected)

	def test_collect_fractions_with_equal_denominators(self):
		f1 = Fraction(1, 5)
		f2 = Fraction(2, 5)

		result = f1 + f2

		expected = Fraction(3, 5)
		self.assertEqual(result, expected)

	def test_str_repr(self):
		fraction = Fraction(1, 3)

		self.assertEqual(str(fraction), "1/3")

	def test_if_simplified_equal_fractions_are_equal(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 2)

		self.assertTrue(f1 == f2)

	def test_if_simplified_non_equal_fractions_are_equal(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)

		self.assertTrue(f1 != f2)

	def test_if_non_simplified_equal_fractions_are_equal(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(2, 4)

		self.assertTrue(f1 == f2)

	def test_if_non_simplified_and_non_equal_fractions_are_equal(self):
		f1 = Fraction(3, 9)
		f2 = Fraction(2, 4)

		self.assertTrue(f1 != f2)

	def test_comparing_fractions(self):
		f1 = Fraction(1, 5)
		f2 = Fraction(2, 5)

		self.assertTrue(f1 < f2)
		self.assertTrue(f1 <= f2)
		self.assertTrue(f2 > f1)
		self.assertTrue(f2 >= f1)
		self.assertTrue(f1 != f2)
		self.assertNotEqual(f1, f2)

	def test_sort_fractions(self):
		fractions = [Fraction(1, 5), Fraction(4, 5), Fraction(3, 5), Fraction(2, 5)]

		sorted_fracrions = sorted(fractions)

		self.assertEqual([Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5)], sorted_fracrions)

	def test_when_denominator_equal_to_0_should_raise_error(self):
		exc = None

		try:
			fraction = Fraction(1, 0)
		except ValueError as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Denominator can not be 0.')

if __name__ == '__main__':
	unittest.main()