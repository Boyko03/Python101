def silence(filename):
    def inner(func):
        def silenced(*argv):
            try:
                return func(*argv)
            except Exception as e:
                with open(filename, 'w') as f:
                    f.write(f"Calling `{func.__name__}` raised an error - {type(e).__name__}: '{e}'. Provided arguments: {argv}.")
        return silenced
    return inner
