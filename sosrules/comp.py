
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

    def __init__(self, interpreter):
        super().__init__()
        self.interpreter = interpreter
    
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
        # This method will produce the smallest possible trees and chains.

        # Unpack the state values
        s, a, p, i, o = state.unpack()
        # Get first legal statement
        index = 1
        if s[0] == "[":
            count = 1
            # Get the corresponding ]
            for c in s[1:]:
                if c == "]":
                    count -= 1
                elif c == "[":
                    count += 1
                index += 1
                if count <= 0:
                    break
            #try:
            #    index = s.rindex("]") + 1
            #except ValueError:
            #    raise Exception("Syntax error detected in program, missing ]")
        # Split the statement into two separate statements
        s1 = s[:index]
        s2 = s[index:]

        # Get the new state from applying a rule
        new_state = self.interpreter.apply_rule(State(s1, a, p, i, o))
        # If the new state is not final, then we append the remaining statement
        # back to statement s2
        if isinstance(new_state, State):
            # Unpack the new state values
            ns, na, np, ni, no = new_state.unpack()
            s2 = ns + s2
        else:
            na, np, ni, no = new_state.unpack()
        # Otherwise, we simply keep s2 and use the new state values
        return State(s2, na, np, ni, no)

    def __repr__(self):
        return "{Comp}"
