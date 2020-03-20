import unittest
from my_sort import my_sort


class TestMySort(unittest.TestCase):
	def test_when_no_args_passed(self):
		result = my_sort()

		expected = []
		self.assertEqual(result, expected)

	def test_when_passing_list_of_integers(self):
		arg = [1, 2, 5, 4, 0]

		result = my_sort(itr=arg)

		expected = [0, 1, 2, 4, 5]
		self.assertEqual(result, expected)

	def test_when_passing_list_of_integers_and_sorting_desc(self):
		arg = [1, 2, 5, 4, 0]

		result = my_sort(itr=arg, asc=False)

		expected = [5, 4, 2, 1, 0]
		self.assertEqual(result, expected)

	def test_when_passing_list_of_chars(self):
		arg = ['a', 'f', 's', 'r', 'b']

		result = my_sort(itr=arg)

		expected = ['a', 'b', 'f', 'r', 's']
		self.assertEqual(result, expected)

	def test_when_passing_empty_tuple(self):
		arg = ()

		result = my_sort(itr=arg)

		expected = ()
		self.assertEqual(result, expected)

	def test_when_passing_tuple_of_integers(self):
		arg = (1, 4, 3, 2)

		result = my_sort(itr=arg)

		expected = (1, 2, 3, 4)
		self.assertEqual(result, expected)

	def test_when_passing_tuple_of_integers_desc(self):
		arg = (1, 4, 3, 2)

		result = my_sort(itr=arg, asc=False)

		expected = (4, 3, 2, 1)
		self.assertEqual(result, expected)

	def test_when_passing_list_of_dictionaries_without_key(self):
		arg = [
			{'name': 'Marto', 'age': 24},
			{'name': 'Ivo', 'age': 27},
			{'name': 'Sashko', 'age': 25}
		]
		exc = None

		try:
			result = my_sort(itr=arg)
		except Exception as e:
			exc = e
		
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Key is required for dictionaries.')

	def test_when_passing_list_of_dictionaries_with_key(self):
		arg = [
			{'name': 'Marto', 'age': 24},
			{'name': 'Ivo', 'age': 27},
			{'name': 'Sashko', 'age': 25}
		]
		key = 'age'

		result = my_sort(itr=arg, key=key)

		expected = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]
		self.assertEqual(result, expected)

	def test_when_passing_list_of_dictionaries_with_key_desc(self):
		arg = [
			{'name': 'Marto', 'age': 24},
			{'name': 'Ivo', 'age': 27},
			{'name': 'Sashko', 'age': 25}
		]
		key = 'age'

		result = my_sort(itr=arg, asc=False, key=key)

		expected = [{'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24}]
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()