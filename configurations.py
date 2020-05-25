
from constants import Statement, Array, Pointer, Input, Output

# Base class for State and FinalState
class Configuration(object):
    def __init__(self):
        super().__init__()
    
    def tex(self) -> str:
        raise NotImplementedError

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

    def __repr__(self) -> str:
        return f"({self.s} | {dict(self.a)} | {self.p} | {repr(self.i)} | {repr(self.o)})"

    def tex(self) -> str:
        # TODO: Change array representation
        return "\sosfive{" + str(self.s) + "}{" + str(dict(self.a)).replace("{", "\{").replace("}", "\}") + "}{" + str(self.p) + "}{" + repr(self.i) + "}{" + repr(self.o) +"}"

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
    
    def tex(self) -> str:
        # TODO: Change array representation
        return "\sosfour{" + str(dict(self.a)) + "}{" + str(self.p) + "}{" + repr(self.i) + "}{" + repr(self.o) +"}"
