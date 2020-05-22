
from constants import Statement, Array, Pointer, Input, Output

# Base class for State and FinalState
class Configuration(object):
    def __init__(self):
        super().__init__()

class State(Configuration):
    def __init__(self, s: Statement, a: Array, p: Pointer, i: Input, o: Output):
        super().__init__()
        self.s = s
        self.a = a
        self.p = p
        self.i = i
        self.o = o
    
    def __repr__(self):
        return f"({self.s} | {self.a} | {self.p} | {self.i} | {self.o})"

class FinalState(Configuration):
    def __init__(self):
        super().__init__()
        self.a = a
        self.p = p
        self.i = i
        self.o = o

    def __repr__(self):
        return f"({self.a} | {self.p} | {self.i} | {self.o})"