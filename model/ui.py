from tkinter import *
from model.model import Model
import re, os

class View:
    
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.root.title("Brainfuck to proof")
        self.root.geometry("400x205")
        self.linterblock = Frame(self.root, width=180)
        self.linterblock.pack_propagate(False)
        self.linterblock.pack(fill=Y, side = LEFT)
        self.inputblock = Frame(self.root)
        self.inputblock.pack(fill="both",expand = True, side = LEFT)
        self.inputblock.pack_propagate(False)

    def renderUI(self):   
        Label(self.linterblock, text="Linting output").pack(fill=X, side=TOP)
        self.proginput = Text(self.inputblock) #Look I really tried to enforce VMC...
        self.proginput.pack(fill='both', expand=True)
        self.warnings = Entry(self.linterblock, state=DISABLED, textvariable=self.model.errors)
        self.warnings.pack(fill=X, side=TOP)
        Label(self.linterblock, text="Max steps in proof").pack(fill=X, side=TOP)
        self.maxsteps = Entry(self.linterblock, textvariable=self.model.maxsteps)
        self.maxsteps.pack(fill=X, side=TOP)
        Label(self.linterblock, text="Actions").pack(fill=X, side=TOP)
        self.format = Button(self.linterblock, text="Auto format program", command=Controller.reformat)
        self.format.pack(fill=X, side=TOP)
        self.flatten = Button(self.linterblock, text="Flatten program", command=Controller.flatten)
        self.flatten.pack(fill=X, side=TOP)
        self.proof = Button(self.linterblock, text="Run interpreter")
        self.proof.pack(fill=X, side=TOP)
        self.converter = Button(self.linterblock, text="Output proof to pdf")
        self.converter.pack(fill=X, side=TOP)
        self.root.mainloop()

view = View()

class Controller:
    @staticmethod
    def runLinter():
        view.model.linter.clean()
        view.model.linter.load(View.proginput.get("1.0",END))
        view.model.errors = view.model.linter.runLinter()

    @staticmethod
    def flatten():
        code = view.proginput.get("1.0",END)
        view.proginput.delete("1.0",END)
        code = re.sub("(\r?\n)|\s", "", code)
        view.proginput.insert("1.0", code)

    @staticmethod
    def reformat():
        Controller.flatten()
        code = view.proginput.get("1.0",END)
        print(code)
        prev = ""
        ilevel = 0
        identfactor = 3
        newcode = ""
        ident = ""
        for char in code:
            if char=="[":
                prev = "["
                ident = " " * ilevel * identfactor
                newcode = f"{newcode}{os.linesep}{ident}["
                ilevel = ilevel + 1
            elif char=="]":
                prev = "]"
                ilevel = ilevel - 1
                ident = " " * ilevel * identfactor
                newcode = f"{newcode}{os.linesep}{ident}]"
            elif char==">":
                ident = " " * ilevel * identfactor
                if prev==">":
                    newcode = f"{newcode}>"
                else:
                    newcode = f"{newcode}{os.linesep}{ident}>"
                prev = ">"
            elif char=="<":
                ident = " " * ilevel * identfactor
                if prev=="<":
                    newcode = f"{newcode}<"
                else:
                    newcode = f"{newcode}{os.linesep}{ident}<"
                prev = "<"
            elif char==",":
                ident = " " * ilevel * identfactor
                if prev==",":
                    newcode = f"{newcode},"
                else:
                    newcode = f"{newcode}{os.linesep}{ident},"
                prev = ","
            elif char==".":
                ident = " " * ilevel * identfactor
                if prev==".":
                    newcode = f"{newcode}."
                else:
                    newcode = f"{newcode}{os.linesep}{ident}."
                prev = "."
            elif char=="+":
                ident = " " * ilevel * identfactor
                if prev==">" or prev=="<" or prev=="+":
                    newcode = f"{newcode}+"
                else:
                   newcode = f"{newcode}{os.linesep}{ident}+" 
                prev = "+"
            elif char=="-":
                ident = " " * ilevel * identfactor
                if prev==">" or prev=="<" or prev=="-":
                    newcode = f"{newcode}-"
                else:
                   newcode = f"{newcode}{os.linesep}{ident}-" 
                prev = "-"
        newcode = newcode[2:]
        view.proginput.delete("1.0",END)
        view.proginput.insert("1.0", newcode)

view.renderUI()

        