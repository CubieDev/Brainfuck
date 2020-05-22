
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from rules import Axiom, Rule

# [S] -> S[S]
# [S] -> ...
# Note that we can combine LoopEnd and LoopBody into one rule Loop and on the fly decide
# which one the two should be applied.
class Loop(Axiom):

    class LoopEnd(Axiom):
        def __init__(self):
            super().__init__()
        
        def __repr__(self):
            return "{LoopEnd}"
    
    class LoopBody(Rule):
        def __init__(self):
            super().__init__()
        
        def __repr__(self):
            return "{LoopBody}"

    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s.startswith("[") and state.s.endswith("]")
    
    def __repr__(self):
        return "{Loop}"