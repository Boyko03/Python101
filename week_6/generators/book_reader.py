def book_reader(book):
    for file in book:
        with open(file, 'r') as f:
            a = f.readline()
            new = a
            while new != '':
                lines = []
                lines.append(new)
                new = f.readline()
                while new != '' and new[0] != '#':
                    lines.append(new)
                    new = f.readline()
                yield ''.join(lines)
