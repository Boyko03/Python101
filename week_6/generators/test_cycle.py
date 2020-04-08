import unittest
from cycle import cycle


class TestCycleGenerator(unittest.TestCase):
    def test_cycle_generator(self):
        iterable = range(0, 10)

        endless = cycle(iterable)

        for item in endless:
            print(item)

        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
