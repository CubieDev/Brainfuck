
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from rules import Axiom, Rule

# ,
class Comma(Axiom):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "," and len(state.i) > 0
    
    def __repr__(self):
        return "{Comma}"