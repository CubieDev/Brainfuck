from model.linter import Linter
import sys
from tkinter import *
from interpreter import Interpreter

class Model():
    def __init__(self):
        self.linter=Linter()
        self.errors = StringVar()
        self.maxsteps = IntVar()
        self.input = StringVar()
        self.name = StringVar()
        self.name.set("Hello world!")
        self.maxsteps.set(1000)
        self.errors.set("Not checked")
        self.interpreter = Interpreter()

        # Proof stats
        self.prooffound = ""
        self.stepstaken = ""
        self.proctime = ""
        self.rulesused = ""

        self.proofseq = ""
        self.prooftree = ""
