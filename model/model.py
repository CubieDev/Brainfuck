from model.linter import Linter
import sys
from tkinter import *
from interpreter import Interpreter

class Model():
    def __init__(self):
        self.linter=Linter()
        self.errors = StringVar()
        self.maxsteps = IntVar()
        self.maxsteps.set(1000)
        self.errors.set("Not checked")
        self.interpreter = Interpreter()
