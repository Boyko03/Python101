import unittest
from solution import solution

class TestSolution(unittest.TestCase):
	def test_if_solution_returns_in_correct_format(self):
		arg = '3x^2'

		result = solution(arg)

		expected = 'The derivative of f(x) = 3x^2 is:\nf\'(x) = 6*x'
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()