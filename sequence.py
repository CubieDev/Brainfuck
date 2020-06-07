
from sosrules.comp import Comp
from configurations import State, FinalState
from rules import Base
from typing import Union

class Step:
    # TODO: Check whether before can be final
    def __init__(self, before: State, rule: Base = None, after: Union[State, FinalState] = None):
        super().__init__()
        self.before = before.copy()
        self.rule = rule
        if after:
            self.after = after.copy()
        else:
            self.after = after

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
        self.steps = []
    
    def add(self, before: State):
        step = Step(before)
        self.steps.append(step)
    
    def length(self):
        return len(self.steps)

    def add_nested(self, before: State, rule: Base, after: Union[State, FinalState]):
        self.steps[-1].nested = Step(before, rule, after)

    def add_after(self, after: Union[State, FinalState], rule: Base, ):
        # TODO: See if it's possible to not have to do this afterward
        self.steps[-1].after = after
        self.steps[-1].rule = rule

#TODO: This must really be fixed and moved to an external template file
    def output(self):
        """
        Captures the trees and configuration chain in a string
        """
        tree = ""
        configSeq = ""
        for c, step in enumerate(self.steps):
            # Note that / will be replaced with \ and < and > are replaced with { and } respectively.

            tree += f"""
/begin«prooftree»
/sctree{"[0px]" if not step.nested else "%"}
  «{step.before.tex()} /Rightarrow {step.after.tex()}»%
  «{step.rule.tex()}»%
  {f'''  «
    /scpremiseleaf%
      «{step.nested.before.tex()} /Rightarrow {step.nested.after.tex()}»%
      «{step.nested.rule.tex()}»%
  »''' if step.nested else '«»'}
/end«prooftree»//
/noindent"""
            configSeq += f"""{'/Rightarrow//' if not c == 0 else ''} {step.before.tex()} {f'/Rightarrow// {step.after.tex()}' if c==(len(self.steps)-1) else ''}"""
        configSeq = configSeq.replace("/", "\\")
        configSeq = '$' + configSeq + '$'
        tree = tree.replace("/", "\\")
        tree = tree.replace("«", "{")
        tree = tree.replace("»", "}")
        return tree, configSeq
