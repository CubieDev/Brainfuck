
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
    
    def apply(self, state: State) -> State:
        # Check whether the state is an actual State object, and the statement inside is of the right form.
        if not self.applicable(state):
            raise Exception(f"State does not support using the {self} rule")
        
        # There exist two Comp rules because where we choose to split up the statement can be arbitrary,
        # as regardless of where we split we always get the same execution.
        # However, in our implementation, we can go for the simplest option which is to just take the first
        # legal statement and try to execute that.

    def __repr__(self):
        return "{Comp}"