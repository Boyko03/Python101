from contextlib import contextmanager


class SilenceException:
    def __init__(self, exc_type, msg=None):
        self.exc_type = exc_type
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        same_exception_type = self.exc_type == exc_type
        correct_message = self.msg is None or self.msg == str(exc_value)

        return same_exception_type and correct_message


@contextmanager
def silence_exception(exc_type, msg=None):
    try:
        yield
    except exc_type as exc:
        if msg is not None and str(exc) != msg:
            raise exc
