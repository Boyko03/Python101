def compress(iterable, mask):
    l_ = len(iterable)
    for i in range(l_):
        if mask[i]:
            yield iterable[i]
