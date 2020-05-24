from tkinter import *

class View:
    def __init__(self):
        self.window = Tk()
        self.window.title("Brainfuck to proof")
        
        Entry(self.window).pack(fill='x')
        Entry(self.window).pack(fill='x')
        self.window.mainloop()

View()