import unittest
from change_decimal_precission import change_precission, ChangePrecission
from decimal import Decimal


class ChangePrecissionContextManagerTests(unittest.TestCase):
    def test_sum_decimals(self):
        with change_precission(2):
            self.assertEqual(Decimal('1.123132132') + Decimal('2.23232'), 3.4)

    def test_multiply_decimals(self):
        with change_precission(2):
            self.assertEqual(Decimal('1.123132132') * Decimal('2.23232'), 2.42)

    def test_sum_decimal_and_float(self):
        with change_precission(2):
            self.assertEqual(Decimal('1.123132132') + 2.2, 3.4)

    def test_changing_precission_only_in_block(self):
        with change_precission(2):
            self.assertEqual(Decimal('1.123132132') + Decimal('2.23232'), 3.4)

        self.assertEqual(Decimal('1.123132132') + Decimal('2.23232'), 3.355452132)


class ChangePrecissionClassTests(unittest.TestCase):
    def test_sum_decimals(self):
        with ChangePrecission(2):
            self.assertEqual(Decimal('1.123132132') + Decimal('2.23232'), 3.4)

    def test_multiply_decimals(self):
        with ChangePrecission(2):
            self.assertEqual(Decimal('1.123132132') * Decimal('2.23232'), 2.42)

    def test_sum_decimal_and_float(self):
        with ChangePrecission(2):
            self.assertEqual(Decimal('1.123132132') + 2.2, 3.4)

    def test_changing_precission_only_in_block(self):
        with ChangePrecission(2):
            self.assertEqual(Decimal('1.123132132') + Decimal('2.23232'), 3.4)

        self.assertEqual(Decimal('1.123132132') + Decimal('2.23232'), 3.355452132)


if __name__ == '__main__':
    unittest.main()
