import unittest
from time import sleep
import time
from performance import performance


class TestPerformanceDecorator(unittest.TestCase):
    def test_performance_decorator_should_write_in_file_time_to_execute(self):
        @performance('performance.txt')
        def test_func():
            sleep(2)

        start = time.time()
        test_func()
        expected = time.time() - start

        with open('performance.txt', 'r') as f:
            result = f.read()

        self.assertEqual(result, f'test_func was called and took {round(expected, 2)} seconds to complete\n')


if __name__ == '__main__':
    unittest.main()
