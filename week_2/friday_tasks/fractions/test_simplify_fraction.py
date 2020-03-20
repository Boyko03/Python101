import unittest
from simplify_fraction import simplify_fraction

class TestSimplifyFraction(unittest.TestCase):
	def test_when_nominator_bigger_than_denominator_and_reducible(self):
		fraction = (9, 3)

		result = simplify_fraction(fraction)

		expected = (3, 1)
		self.assertEqual(result, expected)

	def test_when_nominator_smaller_than_denominator_and_reducible(self):
		fraction = (3, 9)

		result = simplify_fraction(fraction)

		expected = (1, 3)
		self.assertEqual(expected, result)

	def test_when_nominator_bigger_than_denominator_but_not_fully_reducible(self):
		fraction = (462, 63)

		result = simplify_fraction(fraction)

		expected = (22, 3)
		self.assertEqual(result, expected)

	def test_when_nominator_smaller_than_denominator_but_not_fully_reducible(self):
		fraction = (63, 462)

		result = simplify_fraction(fraction)

		expected = (3, 22)
		self.assertEqual(result, expected)

	def test_when_denominator_equal_0_should_return_exception(self):
		fraction = (10, 0)
		exc = None

		try:
			simplify_fraction(fraction)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Dividing by zero.')

if __name__ == '__main__':
	unittest.main()