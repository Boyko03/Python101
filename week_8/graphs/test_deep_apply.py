import unittest
from deep_apply import deep_apply


class DeepApplyTests(unittest.TestCase):
    def test_keys_are_int_and_only_one_layer_of_data_function_increases_them_by_1(self):
        data = {
            1: '1',
            2: '2',
            3: '3'
        }

        def func(key):
            return key + 1

        deep_apply(func, data)
        expected = {
            2: '1',
            3: '2',
            4: '3'
        }

        self.assertEqual(data, expected)

    def test_keys_are_int_and_with_many_layers_of_data_function_increases_them_by_1(self):
        data = {
            1: '1',
            2: '2',
            3: {
                4: '4',
                5: {
                    6: '6'
                }
            }
        }

        def func(key):
            return key + 1

        deep_apply(func, data)
        expected = {
            2: '1',
            3: '2',
            4: {
                5: '4',
                6: {
                    7: '6'
                }
            }
        }

        self.assertEqual(data, expected)

    def test_keys_are_str_and_with_many_layers_of_data_function_increases_them_by_1(self):
        data = {
            '1': '1',
            '2': '2',
            '3': {
                '4': '4',
                '5': {
                    '6': '6'
                }
            }
        }

        def func(key):
            return key + '1'

        deep_apply(func, data)
        expected = {
            '11': '1',
            '21': '2',
            '31': {
                '41': '4',
                '51': {
                    '61': '6'
                }
            }
        }

        self.assertEqual(data, expected)

    # def test_keys_are_not_sorted(self):
    #     data = {
    #         3: '1',
    #         2: '2',
    #         1: '3',
    #         4: '4'
    #     }

    #     def func(key):
    #         return key + 1

    #     deep_apply(func, data)
    #     expected = {
    #         4: '1',
    #         3: '2',
    #         2: '3',
    #         5: '4'
    #     }

    #     self.assertEqual(data, expected)


if __name__ == '__main__':
    unittest.main()
