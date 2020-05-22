
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from rules import Axiom, Rule

# -
class Minus(Axiom):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "-"
    
    def __repr__(self):
        return "{Minus}"