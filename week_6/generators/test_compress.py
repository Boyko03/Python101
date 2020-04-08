import unittest
from compress import compress


class TestCompressGenerator(unittest.TestCase):
    def test_compress_generator(self):
        iterable = ['Ivo', 'Rado', 'Panda', 'Dodo']
        mask = [False, False, True, True]

        result = list(compress(iterable, mask))

        self.assertEqual(result, ['Panda', 'Dodo'])


if __name__ == '__main__':
    unittest.main()
