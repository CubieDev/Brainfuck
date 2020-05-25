
from constants import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from rules import Axiom, Rule, Base

# ,
class Comma(Axiom):
    """The comma rule interprets a character from the input and stores it at p in the array"""
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "," and len(state.i) > 0
    
    def apply(self, state: State) -> (FinalState, Base):
        # Check whether the state is an actual State object, and the statement inside is of the right form.
        if not self.applicable(state):
            raise Exception(f"State does not support using the {self} rule")

        # Unpack the state
        s, a, p, i, o = state.unpack()
        # Apply the Comma rule by setting the currently pointed to value to 
        # the ordinal value corresponding to the first input character
        # and then updating i to remove this first character.
        a[p] = ord(i[0])
        i = i[1:]
        # Return a FinalState with the correct information
        return FinalState(a, p, i, o), self

    def __repr__(self):
        return "{Comma}"
    
    def tex(self) -> str:
        return "\\commasos"