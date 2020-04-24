import unittest
from deep_find import deep_find_bfs, deep_find_dfs


class DeepFindBfsTests(unittest.TestCase):
    def test_without_dict_in_dict(self):
        dict = {
            'key1': 'val1',
            'key2': 'val2'
        }
        key = 'key1'

        result = deep_find_bfs(dict, key)

        self.assertEqual(result, 'val1')

    def test_key_is_in_dict_in_the_dictionary(self):
        dict = {
            'key1': 'val1',
            'key2': 'val2',
            'keys': {
                'key3': 'val3'
            }
        }
        key = 'key3'

        result = deep_find_bfs(dict, key)

        self.assertEqual(result, 'val3')

    def test_with_many_inside_dictionaries_with_many_layers(self):
        dict = {
            'key1': 'val1',
            'key2': 'val2',
            'keys': {
                'key3': 'val3',
                'key4': 'val4',
                'key5': {
                    'key6': 'val6',
                    'key7': 'val7'
                }
            }
        }
        key = 'key7'

        result = deep_find_bfs(dict, key)

        self.assertEqual(result, 'val7')

    def test_function_will_return_the_closest_found_key_if_many_are(self):
        dict = {
            'keys1': {
                'key1': 'val1',
                'keys3': {
                    'key2': 'val2'
                }
            },
            'keys2': {
                'key1': 'val3',
                'key2': 'val4'
            }
        }
        key = 'key2'

        result = deep_find_bfs(dict, key)

        self.assertEqual(result, 'val4')


class DeepFindDfsTests(unittest.TestCase):
    def test_without_dict_in_dict(self):
        dict = {
            'key1': 'val1',
            'key2': 'val2'
        }
        key = 'key1'

        result = deep_find_dfs(dict, key)

        self.assertEqual(result, 'val1')

    def test_key_is_in_dict_in_the_dictionary(self):
        dict = {
            'key1': 'val1',
            'key2': 'val2',
            'keys': {
                'key3': 'val3'
            }
        }
        key = 'key3'

        result = deep_find_dfs(dict, key)

        self.assertEqual(result, 'val3')

    def test_with_many_inside_dictionaries(self):
        dict = {
            'key1': 'val1',
            'key2': 'val2',
            'keys': {
                'key3': 'val3',
                'key4': 'val4',
                'key5': 'val5'
            }
        }
        key = 'key5'

        result = deep_find_dfs(dict, key)

        self.assertEqual(result, 'val5')

    def test_with_many_inside_dictionaries_with_many_layers(self):
        dict = {
            'key1': 'val1',
            'key2': 'val2',
            'keys': {
                'key3': 'val3',
                'key4': 'val4',
                'key5': {
                    'key6': 'val6',
                    'key7': 'val7'
                }
            }
        }
        key = 'key7'

        result = deep_find_dfs(dict, key)

        self.assertEqual(result, 'val7')

    def test_function_will_return_the_first_found_key_if_many_are(self):
        dict = {
            'keys1': {
                'key1': 'val1',
                'key2': 'val2'
            },
            'keys2': {
                'key1': 'val3',
                'key2': 'val4'
            }
        }
        key = 'key2'

        result = deep_find_dfs(dict, key)

        self.assertEqual(result, 'val2')


if __name__ == '__main__':
    unittest.main()
