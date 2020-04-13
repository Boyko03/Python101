import unittest
import curses
from book_reader import book_reader


class TestBookReaderGenerator(unittest.TestCase):
    def test_getting_size_of_window(self):
        book = book_reader(('001.txt', '002.txt'))

        c = ''
        try:
            win = curses.initscr()
            while(c != 'q'):
                c = chr(win.getch())
                win.clear()
                if c == ' ':
                    try:
                        win.addstr(0, 0, next(book))

                    except curses.error:
                        pass
                    except StopIteration:
                        break
        finally:
            curses.endwin()


if __name__ == '__main__':
    unittest.main()
