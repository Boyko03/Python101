def accepts(*argv):
    def inner(func):
        def accepted(**kwargs):
            for arg in kwargs:
                if type(kwargs[arg]) not in argv:
                    error = f'Argument "{arg}" of {func.__name__} is not {argv[0]().__class__.__name__}'
                    if len(argv) > 1:
                        br = 0
                        for arg in argv:
                            if br == 0:
                                br += 1
                                continue
                            error += f' or {arg().__class__.__name__}'

                    error += '!'
                    raise TypeError(error)
            return func(**kwargs)
        return accepted
    return inner
