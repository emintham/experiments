from time import time

class Timer(object):
    def __init__(self):
        self._tstart_stack = []

    def tic(self):
        self._tstart_stack.append(time())

    def toc(self, fmt='Elapsed: %s s'):
        elapsed = time() - self._tstart_stack.pop()
        print fmt % elapsed
        return elapsed


def timeit(func):
    def decorated(**kwargs):
        t = Timer()
        t.tic()
        func(**kwargs)
        t.toc()
    return decorated
