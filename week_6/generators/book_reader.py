import subprocess


def book_reader(book):
    width, heigth = subprocess.check_output(['stty', 'size']).decode().split()
    for file in book:
        with open(file, 'r') as f:
            a = ' '
            while a != '':
                lines = []
                lines += f.readlines(int(heigth) - 1)
                a = f.readline()
                lines.append(a)
                yield ''.join(lines)
