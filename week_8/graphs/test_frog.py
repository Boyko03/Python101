import unittest
from frog import jump, ready, verify, swap_frogs


class ReadyTests(unittest.TestCase):
    def test_ready_should_return_False_if_not_ready(self):
        result = ready('>_<')
        self.assertFalse(result)

        result = ready('><_')
        self.assertFalse(result)

        result = ready('_><')
        self.assertFalse(result)

    def test_ready_should_return_true_if_ready(self):
        result = ready('<_>')

        self.assertTrue(result)


class SwapFrogsTests(unittest.TestCase):
    def test_function_swaps_frog_and_empty_place(self):
        frogs = [frog for frog in 'ab_cd']

        swap_frogs(frogs, -1)

        self.assertEqual(''.join(frogs), 'a_bcd')


class JumpTests(unittest.TestCase):
    def test_with_two_frogs_only(self):
        frogs = [frog for frog in '>_<']

        result = []
        jump(frogs, result)

        expected = '>_<\n_><\n<>_\n<_>\n'
        self.assertEqual(''.join(result), expected)

    def test_with_four_frogs(self):
        frogs = [frog for frog in '>>_<<']

        result = []
        jump(frogs, result)

        expected = ['>>_<<\n', '>_><<\n', '><>_<\n', '><><_\n',
                    '><_<>\n', '_<><>\n', '<_><>\n', '<<>_>\n', '<<_>>\n']
        self.assertEqual(result, expected)


class VerifyTests(unittest.TestCase):
    def test_raises_value_error_if_invalid_symbols_in_frogs(self):
        with self.assertRaises(ValueError, msg='Invalid input.'):
            frogs = 'abc'

            verify(frogs)

    def test_raises_value_error_if_more_than_one_empty_space(self):
        with self.assertRaises(ValueError, msg='Invalid input'):
            frogs = '>_<_'

            verify(frogs)

    def test_raises_value_error_if_missing_frogs(self):
        with self.assertRaises(ValueError, msg='Invalid input.'):
            frogs = '_'

            verify(frogs)

    def test_raises_value_error_if_different_count_of_frogs(self):
        with self.assertRaises(ValueError, msg='Invalid input.'):
            frogs = '>>_<'

            verify(frogs)


if __name__ == '__main__':
    unittest.main()
