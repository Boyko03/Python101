def required(func):
    def after(self, *argv):
        if func.__name__ not in self.__class__.__dict__:
            raise Exception(f'All classes that inherit from "{self.__class__.mro()[1].__name__}" must provide "{func.__name__}" method.')
        return func(self, *argv)
    return after
