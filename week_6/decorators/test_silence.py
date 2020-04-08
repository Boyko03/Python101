import unittest
from silence import silence


class TestSilenceDecorator(unittest.TestCase):
    def test_silence_decorator_when_no_errors_should_not_write_in_file(self):
        @silence('errors.txt')
        def foo(x):
            return x

        result = foo(5)

        self.assertEqual(result, 5)

    def test_silence_decorator_should_write_error_in_file(self):
        @silence('errors.txt')
        def foo(x):
            if x > 50:
                raise ValueError('Omg.')

        foo(10)
        foo(100)

        with open('errors.txt', 'r') as f:
            result = f.read()

        self.assertEqual(result, "Calling `foo` raised an error - ValueError: 'Omg.'. Provided arguments: (100,).")


if __name__ == '__main__':
    unittest.main()
