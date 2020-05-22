

from constants      import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from sosrules.right import Right
from sosrules.left  import Left
from sosrules.plus  import Plus
from sosrules.minus import Minus
from sosrules.dot   import Dot
from sosrules.comma import Comma
from sosrules.comp  import Comp
from sosrules.loop  import Loop

class Interpreter:
    def __init__(self, s: Statement, i: Input = ""):
        super().__init__()
        if not isinstance(s, Statement):
            raise TypeError("Program must be passed as a str object.")
        if not isinstance(i, Input):
            raise TypeError("Input must be passed as a str object.")

        # Set up list of Rules to be used
        self.rules = [
            Right(),
            Left(),
            Plus(),
            Minus(),
            Dot(),
            Comma(),
            Comp(),
            Loop()
        ]

        # Initialize state variables
        a = dict()
        p = 0
        o = ""
        initial_state = State(s, a, p, i, o)

        self.parse(initial_state)
    
    def parse(self, state: State):
        print(state)
        for rule in self.rules:
            if rule.applicable(state):
                print(rule)
                new_state = rule.apply(state)
                break
        else:
            # Stuck
            return
        print(new_state, rule)
        
if __name__ == "__main__":
    program = "++>,<[->+<]>."
    Interpreter(program)
