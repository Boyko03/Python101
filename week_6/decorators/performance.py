import time


def performance(file):
    def inner(func):
        def modified_func(*argv):
            start_time = time.time()
            func(*argv)
            with open(file, 'a') as f:
                f.write(f'{func.__name__} was called and took {round(time.time() - start_time, 2)} seconds to complete\n')
        return modified_func
    return inner
