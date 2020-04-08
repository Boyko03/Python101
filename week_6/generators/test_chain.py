import unittest
from chain import chain


class TestChainGenerator(unittest.TestCase):
    def test_chain_with_range_to_list(self):
        iterable_one = range(0, 4)
        iterable_two = range(4, 8)

        result = list(chain(iterable_one, iterable_two))

        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
