
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from rules import Axiom, Rule, Base

from typing import Union # Read as: Either

# [S] -> S[S]
# [S] -> ...
# Note that we can combine LoopEnd and LoopBody into one rule Loop and on the fly decide
# which one the two should be applied.
class Loop(Base):

    class LoopEnd(Axiom):
        def __init__(self):
            super().__init__()
        
        def applicable(self, state: State) -> bool:
            return state.a[state.p] == 0

        def apply(self, state: State) -> (FinalState, Base):
            # Check whether the state is an actual State object, and the statement inside is of the right form.
            if not self.applicable(state):
                raise Exception(f"State does not support using the {self} rule")

            # Unpack the information from the given state
            s, a, p, i, o = state.unpack()
            # And create a FinalState with these state values
            return FinalState(a, p, i, o), self

        def __repr__(self) -> str:
            return "{LoopEnd}"
        
        def tex(self) -> str:
            return "\\emptyloopsos"
    
    class LoopBody(Rule):
        def __init__(self):
            super().__init__()
        
        def applicable(self, state: State) -> bool:
            return state.a[state.p] != 0
        
        def apply(self, state: State) -> (State, Base):
            # Check whether the state is an actual State object, and the statement inside is of the right form.
            if not self.applicable(state):
                raise Exception(f"State does not support using the {self} rule")

            # Unpack the information from the given state
            s, a, p, i, o = state.unpack()
            # And create a State by prepending S to the [S]. 
            # We can do this by slicing off the first and last index from s
            s = s[1:-1] + s
            return State(s, a, p, i, o), self

        def __repr__(self) -> str:
            return "{LoopBody}"
        
        def tex(self) -> str:
            return "\\loopsos"

    def __init__(self):
        super().__init__()
        self.lb = self.LoopBody()
        self.le = self.LoopEnd()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        if state.s.startswith("[") and state.s.endswith("]"):
            # For the statement to be applicable, the first and last bracket must be related,
            # eg not "[]+[]"
            # we can confirm this by checking whether the statement with 
            # these two brackets removed is valid or not.
            count = 0
            for c in state.s[1:-1]:
                if c == "[":
                    count += 1
                elif c == "]":
                    count -= 1
                if count < 0:
                    return False
            return True

    def apply(self, state: State) -> (Union[State, FinalState], Base): # Read as: Either State or FinalState, alongside Base
        # Check whether the state is an actual State object, and the statement inside is of the right form.
        if not self.applicable(state):
            raise Exception(f"State does not support using the {self} rule")

        # Use applicable to determine whether we should use LoopBody or LoopEnd
        # and then apply with those rules
        if self.lb.applicable(state):
            return self.lb.apply(state)
        elif self.le.applicable(state):
            return self.le.apply(state)
        raise Exception("Neither Loop Rule seems applicable.")

    def __repr__(self) -> str:
        return "{Loop}"

    # tex is not implemented for this class