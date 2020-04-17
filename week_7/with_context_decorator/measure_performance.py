import time
import os


class MeasurePerformance:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self._benchmarks = []

    def __enter__(self):
        self.file = open(self.filename, 'w')

        self.original_start = time.time()
        self.start = self.original_start

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            if exc_type:
                self.file.close()
                os.remove(self.filename)
            else:
                self.file.write('\n'.join(self._benchmarks))
                self.file.write(f'\nFinished for: {int(time.time() - self.original_start)}s')
                self.file.close()

    def benchmark(self, msg=None, restart=False):
        if msg is None:
            msg = f'Benchmark No.{len(self._benchmarks) + 1}'

        msg += f': {int(self.get_exceeded_time())}s'
        self._benchmarks.append(msg)

        if restart:
            self.start = time.time()

    def get_exceeded_time(self):
        return time.time() - self.start
