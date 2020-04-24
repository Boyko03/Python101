import unittest
from deep_update import deep_update


class DeepUpdateTests(unittest.TestCase):
    def test_does_not_update_anything_if_key_not_in_dict(self):
        data = {
            'k1': 'v1',
            'k2': 'v2'
        }
        orig_data = data
        key = 'k3'
        val = 'v3'

        deep_update(data, key, val)

        self.assertEqual(data, orig_data)

    def test_updates_every_occurance_of_given_key_in_data_with_val(self):
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
        val = 1
        expected = {
            'keys1': {
                'key1': 1,
                'keys2': {
                    'key1': 1
                }
            },
            'key1': 1,
            'keys2': {
                'key1': 1
            }
        }

        deep_update(data, key, val)

        self.assertEqual(data, expected)


if __name__ == '__main__':
    unittest.main()
