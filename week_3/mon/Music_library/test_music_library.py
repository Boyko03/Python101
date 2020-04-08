import unittest
from music_library import Song

class TestSong(unittest.TestCase):
	def test_init_and_str(self):
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

		result = str(s)

		expected = 'Manowar - Odin from The Sons of Odin - 3:44'
		self.assertEqual(result, expected)

	def test_if_length_is_invalid_should_raise_error(self):
		pass

if __name__ == '__main__':
	unittest.main()