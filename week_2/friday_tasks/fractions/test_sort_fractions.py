import unittest
from sort_fractions import sort_fractions

class TestSortFractions(unittest.TestCase):
	def test_when_sorting_ascending_and_denominators_are_equal(self):
		fractions = [(4, 5), (2, 5), (3, 5), (1, 5)]

		result = sort_fractions(fractions, asc=True)

		expected = [(1, 5), (2, 5), (3, 5), (4, 5)]
		self.assertEqual(result, expected)

	def test_when_sorting_descending_and_denominators_are_equal(self):
		fractions = [(4, 5), (2, 5), (3, 5), (1, 5)]

		result = sort_fractions(fractions, asc=False)

		expected = [(4, 5), (3, 5), (2, 5), (1, 5)]
		self.assertEqual(result, expected)

	def test_when_sorting_ascending_and_denominators_are_different(self):
		fractions = [(2, 3), (1, 2), (1, 3)]

		result = sort_fractions(fractions)

		expected = [(1, 3), (1, 2), (2, 3)]
		self.assertEqual(result, expected)

	def test_when_sorting_descending_and_denominators_are_different(self):
		fractions = [(2, 3), (1, 2), (1, 3)]

		result = sort_fractions(fractions, False)

		expected = [(2, 3), (1, 2), (1, 3)]
		self.assertEqual(result, expected)

	def test_when_sorting_with_multiple_fractions_and_without_asc_parameter(self):
		fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]

		result = sort_fractions(fractions)

		expected = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()