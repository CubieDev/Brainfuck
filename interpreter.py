
from collections import defaultdict
import re, datetime
from typing import Union

from constants      import Statement, Array, Pointer, Input, Output
from configurations import State, FinalState
from sequence       import Sequence
from rules          import Base, Error
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

class Interpreter():
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
        self.rulecount = {
            Right().tex(): 0,
            Left().tex(): 0,
            Plus().tex(): 0,
            Minus().tex(): 0,
            Dot().tex(): 0,
            Comma().tex(): 0,
            Loop.LoopBody().tex():0,
            Loop.LoopEnd().tex():0,
            Comp.CompOne().tex():0,
            Comp.CompTwo().tex():0
        }
        self.sequence = Sequence()
        # Strip the program of characters that aren't in the language
        self.s = re.sub("[^\<\>\,\.\[\]\-\+]", "", s)

        # Initialize state variables
        a = defaultdict(lambda: 0)
        p = 0
        o = ""
        self.initial_state = State(s, a, p, i, o)
        self.stepcount = 0

        if(len(self.s) > 0):
            self.parse(self.initial_state)
    
    #TODO: fix this
    def initialize(self, program, input=""):
        if not isinstance(program, Statement):
            raise TypeError("Program must be passed as a str object.")
        if not isinstance(program, Input):
            raise TypeError("Input must be passed as a str object.")

        self.s = re.sub("[^\<\>\,\.\[\]\-\+]", "", program)

        self.rulecount = { # Reset rulecount
            Right().tex(): 0,
            Left().tex(): 0,
            Plus().tex(): 0,
            Minus().tex(): 0,
            Dot().tex(): 0,
            Comma().tex(): 0,
            Loop.LoopBody().tex():0,
            Loop.LoopEnd().tex():0,
            Comp.CompOne().tex():0,
            Comp.CompTwo().tex():0
        }
        # Initialize state variables
        a = defaultdict(lambda: 0)
        p = 0
        o = ""
        self.initial_state = State(self.s, a, p, input, o)

    def run_interpreter(self, max=100000):
        now = datetime.datetime.now()
        c = 0
        try:
            if(len(self.s) > 0):
                for c, _ in enumerate(self.parse(self.initial_state)):
                    if c >= max:
                        return self.rulecount, c, False, (datetime.datetime.now() - now).total_seconds()
                    print(c)
        except EmptyInputException:
            self.sequence.add(FinalState(err=True))
            self.sequence.add_after(FinalState(err=True), Error())
            return self.rulecount, c, False, (datetime.datetime.now() - now).total_seconds()

        return self.rulecount, c, True, (datetime.datetime.now() - now).total_seconds()

    def parse(self, state: State):
        # For now this only applies one rule
        #print(state)
        #print(new_state, rule)
        while True:
            state, rule = self.apply_rule(state, new=True)
            self.sequence.add_after(state, rule)
            if isinstance(state, FinalState):
                break
            else: 
                yield "non final"
            #breakpoint()
    
    def apply_rule(self, state: State, new = False) -> (Union[State, FinalState], Base):
        for rule in self.rules:
            if rule.applicable(state):
                if new:
                    self.sequence.add(state)
                new_state, applied_rule = rule.apply(state)
                self.rulecount[applied_rule.tex()] += 1
                return new_state, applied_rule
        else:
            # Stuck
            raise EmptyInputException("Stuck state reached")

# if __name__ == "__main__":
#     i = ""
#     #program = "++>,<[->+<]>."
#     #program = ","
#     #program = "[<->]+"
#     program = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++"
#     ip = Interpreter()
#     ip.initialize(program,i)
#     rulec, c, final, time = ip.run_interpreter()
#     _, seq = ip.sequence.output()
#     print(time.total_seconds())
#     print(final)
#     print(c)
#     print(rulec)
#     #breakpoint()
