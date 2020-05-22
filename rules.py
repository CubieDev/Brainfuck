
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState

# Base class for Rules and Axioms
class Base(object):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        if not isinstance(state, State):
            raise TypeError("You can only check applicability of this rule using a State instance.")

class Axiom(Base):
    def __init__(self):
        super().__init__()

    def apply(self, state: State) -> FinalState:
        raise NotImplementedError
    
class Rule(Base):
    def __init__(self):
        super().__init__()
    
    def apply(self, state: State) -> State:
        raise NotImplementedError