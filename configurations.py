
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
    
    def unpack(self) -> (Statement, Array, Pointer, Input, Output):
        return self.s, self.a, self.p, self.i, self.o

    def __repr__(self):
        return f"({self.s} | {dict(self.a)} | {self.p} | {repr(self.i)} | {repr(self.o)})"

class FinalState(Configuration):
    def __init__(self, a: Array, p: Pointer, i: Input, o: Output):
        super().__init__()
        self.a = a
        self.p = p
        self.i = i
        self.o = o
    
    def unpack(self) -> (Array, Pointer, Input, Output):
        return self.a, self.p, self.i, self.o

    def __repr__(self):
        return f"({dict(self.a)} | {self.p} | {repr(self.i)} | {repr(self.o)})"