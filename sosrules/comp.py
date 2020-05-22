
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from rules import Axiom, Rule

# S_1S_2 -> S_1'S_2
# S_1S_2 -> S_2
# Note that we can combine CompOne and CompTwo into one rule Comp and on the fly decide
# which one the two should be applied.
class Comp(Rule):

    class CompOne(Rule):
        def __init__(self):
            super().__init__()
        
        def __repr__(self):
            return "{CompOne}"
    
    class CompTwo(Rule):
        def __init__(self):
            super().__init__()
        
        def __repr__(self):
            return "{CompTwo}"

    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return len(state.s) > 1
    
    def __repr__(self):
        return "{Comp}"