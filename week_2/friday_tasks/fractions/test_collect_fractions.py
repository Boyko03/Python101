import unittest
from collect_fractions import collect_fractions

class TestCollectFractions(unittest.TestCase):
	def test_when_only_one_fraction_should_return_simplified_fraction(self):
		fractions = [(2, 4)]

		result = collect_fractions(fractions)

		expected = (1, 2)
		self.assertEqual(result, expected)

	def test_collect_fractions_with_common_denominator(self):
		fractions = [(1, 5), (3, 5)]

		result = collect_fractions(fractions)

		expected = (4, 5)
		self.assertEqual(result, expected)

	def test_when_two_fractions_and_different_denominators(self):
		fractions = [(1, 2), (1, 4)]

		result = collect_fractions(fractions)

		expected = (3, 4)
		self.assertEqual(result, expected)

	def test_with_two_fractions_and_nominator_and_denominator_different(self):
		fractions = [(1, 7), (2, 6)]

		result = collect_fractions(fractions)

		expected = (10, 21)
		self.assertEqual(result, expected)

	def test_with_multiple_fractions(self):
		fractions = [(1, 2), (2, 3), (3, 4)]

		result = collect_fractions(fractions)

		expected = (23, 12)
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()