import unittest
from frog import jump, ready, frog_jump


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


class FrogJumpTests(unittest.TestCase):
    def test_function_swaps_frog_and_empty_place(self):
        frogs = [frog for frog in 'ab_cd']

        frog_jump(frogs, -1)

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


if __name__ == '__main__':
    unittest.main()
