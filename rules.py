
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState

# Base class for Rules and Axioms
class Base(object):
    """Base abstract class that requires applicable overload"""

    def applicable(self, state: State) -> bool:
        if not isinstance(state, State):
            raise TypeError("You can only check applicability of this rule using a State instance.")

    def tex(self) -> str:
        raise NotImplementedError

class Axiom(Base):
    def apply(self, state: State) -> (FinalState, Base):
        raise NotImplementedError
    
class Rule(Base):
    def apply(self, state: State) -> (State, Base):
        raise NotImplementedError

class Error(Rule):
    """Generic error class"""

    def __init__(self):
        super().__init__()
    
    def __repr__(self) -> str:
        return "{NoRule}"
    
    def tex(self) -> str:
        return "\\error"