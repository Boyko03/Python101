import unittest
from deep_find_all import deep_find_all_bfs, deep_find_all_dfs


class DeepFindAllBfsTests(unittest.TestCase):
    def test_bfs_finds_all_values_in_the_correct_order(self):
        data = {
            'keys1': {
                'key1': 'val3',
                'keys2': {
                    'key1': 'val4'
                }
            },
            'key1': 'val1',
            'keys2': {
                'key1': 'val5'
            }
        }
        key = 'key1'

        expected = ['val1', 'val3', 'val5', 'val4']
        result = deep_find_all_bfs(data, key)

        self.assertEqual(result, expected)


class DeepFindAllDfsTests(unittest.TestCase):
    def test_dfs_finds_all_values_in_the_correct_order(self):
        data = {
            'keys1': {
                'key1': 'val3',
                'keys2': {
                    'key1': 'val4'
                }
            },
            'key1': 'val1',
            'keys2': {
                'key1': 'val5'
            }
        }
        key = 'key1'

        expected = ['val1', 'val3', 'val4', 'val5']
        result = deep_find_all_dfs(data, key)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
