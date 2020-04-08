import unittest
from accepts import accepts


class TestAccepts(unittest.TestCase):
    def test_function_accepts_args_of_type_str_and_given_str(self):
        @accepts(str)
        def say_hello(name):
            pass

        exc = None
        try:
            say_hello(name='Boyko')
        except Exception as e:
            exc = e

        self.assertIsNone(exc)

    def test_function_accepts_args_of_type_str_should_raise_error_if_arg_of_type_int(self):
        @accepts(str)
        def say_hello(name):
            pass

        exc = None
        try:
            say_hello(name=1)
        except TypeError as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument "name" of say_hello is not str!')

    def test_function_accepts_multiple_arguements_of_different_types_returns_true_if_correct(self):
        @accepts(str, int)
        def deposit(name, money):
            pass

        exc = None
        try:
            deposit(name="Marto", money=10)
        except Exception as e:
            exc = e

        self.assertIsNone(exc)

    def test_function_accepts_multiple_arguements_of_different_types_returns_false_if_not_correct(self):
        @accepts(str, int)
        def deposit(name, money):
            pass

        exc = None
        try:
            deposit(name="Marto", money=(1, 5))
        except Exception as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument "money" of deposit is not str or int!')


if __name__ == '__main__':
    unittest.main()
