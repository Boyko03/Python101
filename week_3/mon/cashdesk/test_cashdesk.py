import unittest
from cashdesk import Bill

class TestBill(unittest.TestCase):
	def test_initialization(self):
		amount = 10
		bill = Bill(amount)

		self.assertEqual(bill.amount, amount)

	def test_initialization_with_invalid_amounts_should_raise_value_errors(self):
		err = 'Invalid type.'
		exc = None
		try:
			bill = Bill(1.5)
		except TypeError as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), err)

		exc = None
		try:
			bill = Bill('1')
		except TypeError as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), err)

		exc = None
		try:
			bill = Bill('abc')
		except TypeError as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), err)

		exc = None
		try:
			bill = Bill(-5)
		except ValueError as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid value.')

		exc = None
		try:
			bill = Bill((1,))
		except TypeError as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), err)

	def test_repr_and_str(self):
		bill = Bill(10)

		self.assertEqual(int(bill), 10)
		self.assertEqual(str(bill), 'A 10$ bill')

	def test_if_bills_are_equal(self):
		a = Bill(10)
		b = Bill(9)
		c = Bill(10)

		self.assertTrue(a != b)
		self.assertTrue(a == c)

if __name__ == '__main__':
	unittest.main()