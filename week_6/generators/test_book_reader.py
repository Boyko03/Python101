import unittest
import sys
from book_reader import book_reader


class TestBookReaderGenerator(unittest.TestCase):
    def test_getting_size_of_window(self):
        book = book_reader(('001.txt', '002.txt'))

        c = ''
        while(c != 'q'):
            c = sys.stdin.read(1)
            if c == ' ':
                try:
                    print(next(book))
                except StopIteration:
                    print('End of book')
                    break


if __name__ == '__main__':
    unittest.main()
