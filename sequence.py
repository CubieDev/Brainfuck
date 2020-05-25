
from sosrules.comp import Comp

class Step:
    def __init__(self, before, rule):
        super().__init__()
        self.before = before
        self.rule = rule
        
        self.after = None
        self.nested = None

    def __repr__(self):
        out = ""
        if self.nested:
            out = str(self.nested)
            out += '-' * len(out) + "\n"
        if self.after:
            return f"{out}{self.before} => {self.after}^{self.rule}\n"
        return f"{out}{self.before}^{self.rule}\n"

class Sequence:
    def __init__(self):
        super().__init__()
        self.last_step = None
        self.states = []
    
    def add(self, state, rule):
        
        step = Step(state, rule)
        # If the previous rule was a Comp rule, we want to absorb 
        # this step as a nested step into that step, instead of adding it as a new step.
        if self.last_step and isinstance(self.last_step.rule, Comp):
            self.states[-1].nested = step
        else:
            self.states.append(step)
        self.last_step = step
    
    def add_after(self, state):
        if self.last_step:
            self.last_step.after = state
    
    