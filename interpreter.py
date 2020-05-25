
from collections import defaultdict
import re

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

class EmptyInputException(Exception):
    pass

class Interpreter:
    def __init__(self, s: Statement = "", i: Input = ""):
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
            Loop(),
            Comp(self) # Composition takes an instance of Interpreter as it will want to execute a rule.
        ]

        # Strip the program of characters that aren't in the language
        s = re.sub("[^\<\>\,\.\[\]\-\+]", "", s)

        # Initialize state variables
        a = defaultdict(lambda: 0)
        p = 0
        o = ""
        initial_state = State(s, a, p, i, o)

        if(len(s) > 0):
            self.parse(initial_state)
    
    #TODO: fix this
    def initialize(self, program, input=""):
        if not isinstance(s, Statement):
            raise TypeError("Program must be passed as a str object.")
        if not isinstance(i, Input):
            raise TypeError("Input must be passed as a str object.")
        s = re.sub("[^\<\>\,\.\[\]\-\+]", "", s)
        #etc

    def parse(self, state: State):
        # For now this only applies one rule
        #print(state)
        #print(new_state, rule)
        while True:
            state = self.apply_rule(state)
            if isinstance(state, FinalState):
                break
            #breakpoint()
    
    def apply_rule(self, state: State):
        for rule in self.rules:
            if rule.applicable(state):
                print(rule)
                new_state = rule.apply(state)
                print(new_state)
                return new_state
        else:
            # Stuck
            print("Stuck state reached")
            raise EmptyInputException()

if __name__ == "__main__":
    #i = "a"
    #program = "++>,<[->+<]>."
    #program = "[<->]+"
    program = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    Interpreter(program)
