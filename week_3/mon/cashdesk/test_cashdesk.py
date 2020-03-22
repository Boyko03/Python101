import unittest
from cashdesk import Bill, BillBatch, CashDesk

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

	def test_hash_function(self):
		money_holder = {}
		a = Bill(10)
		b = Bill(10)

		money_holder[a] = 1
		if b in money_holder:
			money_holder[b] += 1

		expexted = 2
		self.assertEqual(expexted, money_holder[a])

	def test_int_function(self):
		a = Bill(10)

		result = int(a)

		expexted = 10
		self.assertEqual(result, expexted)

class TestBatchBill(unittest.TestCase):
	def test_get_len_of_bill_batch(self):
		values = [10, 20, 50, 100]
		bills = [Bill(value) for value in values]

		batch = BillBatch(bills)

		self.assertEqual(len(batch), 4)

	def test_total(self):
		values = [10, 20, 50, 100]
		bills = [Bill(value) for value in values]

		batch = BillBatch(bills)
		total = batch.total()

		expexted = 180
		self.assertEqual(total, expexted)

	def test_iteration_of_bill_batch(self):
		values = [10, 20, 50, 100]
		bills = [Bill(value) for value in values]
		batch = BillBatch(bills)

		result = ""
		for bill in batch:
			result += f'{bill}\n'

		expexted = "A 10$ bill\nA 20$ bill\nA 50$ bill\nA 100$ bill\n"
		self.assertEqual(result, expexted)

class TestCashDesk(unittest.TestCase):
	def test_take_money_batch(self):
		values = [10, 20, 50, 100, 100, 100]
		bills = [Bill(value) for value in values]

		batch = BillBatch(bills)

		desk = CashDesk()

		desk.take_money(batch)

	def test_total_if_cash_desk_is_empty(self):
		values = [10, 20, 50, 100, 100, 100]
		bills = [Bill(value) for value in values]
		batch = BillBatch(bills)
		desk = CashDesk()

		result = desk.total()

		expexted = 0
		self.assertEqual(result, expexted)

	def test_total_when_cash_desk_is_not_empty(self):
		values = [10, 20, 50, 100, 100, 100]
		bills = [Bill(value) for value in values]
		batch = BillBatch(bills)
		desk = CashDesk()

		desk.take_money(batch)
		desk.take_money(Bill(10))
		result = desk.total()

		expexted = 390
		self.assertEqual(result, expexted)

	def test_inspect_function(self):
		values = [10, 20, 50, 100, 100, 100]
		bills = [Bill(value) for value in values]
		batch = BillBatch(bills)
		desk = CashDesk()

		desk.take_money(batch)
		desk.take_money(Bill(10))
		
		desk.inspect()

if __name__ == '__main__':
	unittest.main()