def chain(iterable_one, iterable_two):
    for i in iterable_one:
        yield i

    for i in iterable_two:
        yield i
