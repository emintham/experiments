from contextlib import contextmanager
from tictoc import timeit

def with_bar(func):
    def decorated(self):
        self.bar = 1
        func(self)
    return decorated

class Mixin(object):
    @contextmanager
    def foo(self):
        self.bar = 1
        yield


class A(object):
    def __init__(self):
        self.data = 0


class B(A): pass # dummy class to make inheritance longer


class C(B, Mixin):
    def baz(self):
        with self.foo():
            self.data += self.bar


class D(B):
    @with_bar
    def baz(self):
        self.data += self.bar


@timeit
def execute_c(n):
    c = C()
    for _ in range(n):
        c.baz()
    print 'c.data = {}'.format(c.data)

@timeit
def execute_d(n):
    d = D()
    for _ in range(n):
        d.baz()
    print 'd.data = {}'.format(d.data)

N = 1000000
print 'Testing @contextmanager'
execute_c(n=N)

print ''
print 'Testing decorator'
execute_d(n=N)
