from contextlib import contextmanager
from decimal import getcontext


@contextmanager
def change_precission(precission):
    prec = getcontext().prec
    try:
        getcontext().prec = precission
        yield
    except Exception:
        pass
    finally:
        getcontext().prec = prec


class ChangePrecission:
    def __init__(self, precission):
        self.prec = precission
        self.original_prec = getcontext().prec

    def __enter__(self):
        getcontext().prec = self.prec

    def __exit__(self, exc_type, exc_value, exc_traceback):
        getcontext().prec = self.original_prec
