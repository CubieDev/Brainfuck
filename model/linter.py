import re


##Potential but VERY HARD linting: check if loop limiter is divided by decrements of loop limited, check if input is long enough to run proof
##Trust me I tried. They're logically very hard both. Just leave this by the wayside, it's fun but not worth the effort
class Linter():
    """The linter detects basic errors with the program"""

    def __init__(self):
        self.flags = 0b0000
        self.program = ""

    def load(self, progr):
        self.program = progr
        self.program = re.sub("[^\<\>\,\.\[\]\-\+]", "", self.program)
    
    def clean(self):
        self.flags = 0b0000
        self.program = ""

    def run_linter(self):
        self.flags = self.check_bracket_placement()
        self.flags = self.check_unnecessary_loop()
        return "OK" if self.flags==0 else ("Redundant loop" if self.flags==1 else ("Illegal brackets" if self.flags==2 else "Illegal brackets, redundant loop"))
    
    def check_unnecessary_loop(self):
        """Checks whether a loop is irrelevant"""
        valAr = [0]
        curP = 0
        func = {
           '>': lambda ar, i: (ar, i+1),
           '<': lambda ar, i: (ar, i-1),
           '+': lambda ar, i: (ar+1, i),
           '-': lambda ar, i: (ar-1, i),
           ',': lambda ar, i: (ar, i),
           '.': lambda ar, i: (ar, i)
        }
        for char in self.program:
            if char=='[':
                if valAr[curP] == 0:
                    return self.flags | 0b0001
            elif char==']':
                continue
            else:
                if char in func:
                    valAr[curP], curP = func[char](valAr[curP], curP)
                    if(len(valAr) <= curP):
                        valAr.append(0)
        return self.flags

    def check_bracket_placement(self):
        """Checks whether the bracket placement is legal"""
        brC = 0
        for char in self.program:
            if char=="[":
                brC = brC + 1
            elif char=="]":
                brC = brC - 1
                if brC < 0:
                    return (self.flags | 0b0010)
        
        return (self.flags | 0b0010) if not brC == 0 else self.flags 
