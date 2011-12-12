import copy
import time
from Tkinter import *
import tkMessageBox

import desk


class App:

    def __init__(self, master):
        matrixframe = Frame(master)
        matrixframe.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.desk = desk.Desk(master=matrixframe, background='#ffffff', width=600, height=600, rows=10, cols=10)
        self.desk.pack(side=LEFT, fill=BOTH, expand=1)
        self.desk.bind('<Button-1>', self.user_update_cell)
    
    def user_update_cell(self, event):
        cell = self.desk.get_cell_by_coords(event.x, event.y)
        self.desk.update_cell(cell)
        

        
root = Tk()
root.title("Python Tkinter implementation of Game of Life, by Taras Bilynskyi")
app = App(root)
root.mainloop()
