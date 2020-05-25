
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from rules import Axiom, Rule, Base

# <
class Left(Axiom):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "<"
    
    def apply(self, state: State) -> (FinalState, Base):
        # Check whether the state is an actual State object, and the statement inside is of the right form.
        if not self.applicable(state):
            raise Exception(f"State does not support using the {self} rule")
        
        # Unpack the state
        s, a, p, i, o = state.unpack()
        # Apply the Left rule by decrementing data pointer
        p -= 1
        # Return a FinalState with the correct information
        return FinalState(a, p, i, o), self

    def __repr__(self) -> str:
        return "{Left}"
    
    def tex(self) -> str:
        return "\\leftsos"