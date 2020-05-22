
Statement = str
# We can use a dict to easily represent our Array, 
# as we can then use negative and very large pointers, just like in our rules.
Array = dict
Pointer = int
Input = str
Output = str

# Base class for 
class Configuration(object):
    def __init__(self):
        super().__init__()

class State(Configuration):
    def __init__(self, s: Statement, a: Array, p: Pointer, i: Input, o: Output):
        super().__init__()
        self.s = s
        self.a = a
        self.p = p
        self.i = i
        self.o = o
    
    def __repr__(self):
        return f"({self.s} | {self.a} | {self.p} | {self.i} | {self.o})"

class FinalState(Configuration):
    def __init__(self):
        super().__init__()
        self.a = a
        self.p = p
        self.i = i
        self.o = o

    def __repr__(self):
        return f"({self.a} | {self.p} | {self.i} | {self.o})"

# Base class for Rules and Axioms
class Base(object):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        if not isinstance(state, State):
            raise TypeError("You can only check applicability of this rule using a State instance.")

class Axiom(Base):
    def __init__(self):
        super().__init__()

    def apply(self, state: State) -> FinalState:
        raise NotImplementedError
    
class Rule(Base):
    def __init__(self):
        super().__init__()
    
    def apply(self, state: State) -> State:
        raise NotImplementedError

# >
class Right(Axiom): 
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == ">"
    
    def __repr__(self):
        return "{Right}"

# <
class Left(Axiom):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "<"
    
    def __repr__(self):
        return "{Left}"
# +
class Plus(Axiom):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "+"
    
    def __repr__(self):
        return "{Plus}"

# -
class Minus(Axiom):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "-"
    
    def __repr__(self):
        return "{Minus}"
# .
class Dot(Axiom):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "."
    
    def __repr__(self):
        return "{Dot}"
# ,
class Comma(Axiom):
    def __init__(self):
        super().__init__()
    
    def applicable(self, state: State) -> bool:
        super().applicable(state)
        return state.s == "," and len(state.i) > 0
    
    def __repr__(self):
        return "{Comma}"

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

class Interpreter:
    def __init__(self, s: Statement, i: Input = ""):
        super().__init__()
        if not isinstance(s, Statement):
            raise TypeError("Program must be passed as a str object.")
        if not isinstance(i, Input):
            raise TypeError("Input must be passed as a str object.")
        # TODO: Empty program?

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
