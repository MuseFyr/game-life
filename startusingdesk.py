import copy
import time
from Tkinter import *
import tkMessageBox

import gamelife
import desk

init_filled = [
               (4,5),(4,6),(4,7),
               (5,5),(5,6),(5,7),
               (6,5),(6,6),(6,7),
                              
               (7,8),(7,9),(7,10),
               (8,8),(8,9),(8,10),
               (9,8),(9,9),(9,10),
               ]

init_filled = [
               (7,7),(8,7),(9,7),(9,8),(9,9),(8,9),(7,9)
               ]

init_filled = [
               (6,6),(6,7),(6,8),(7,8),(8,8),(8,9),(8,10)
               ]
#
#init_filled = [
#               (7,9),(8,8),(8,9),(8,10)
#               ]


class App:

    def __init__(self, master):
        matrixframe = Frame(master)
        matrixframe.pack(side=LEFT, fill=BOTH, expand=1)
        self.desk = desk.Desk(master=matrixframe, background='#ffffff', width=600, height=600)
        self.desk.pack(side=LEFT, fill=BOTH, expand=1)
        self.desk.bind('<Button-1>', self.user_update_cell)
        
        sideframe = Frame(master)
        sideframe.pack()
                
        delay_frame = Frame(sideframe)
        delay_frame.pack(side=TOP)
        
        dealy_label = Label(delay_frame, text="Delay (ms)")
        dealy_label.pack(side=LEFT)        
        delay_var = StringVar()
        delay_var.set(100)
        self.delay_field = Entry(delay_frame, width="5", textvariable=delay_var)
        self.delay_field.pack(side=LEFT)
        set_delay_button = Button(delay_frame, text="Set delay", command=self.set_delay)
        set_delay_button.pack(side=LEFT)
        
        config_frame = Frame(sideframe)
        config_frame.pack(side=TOP)
        
        n_label = Label(config_frame, text="Rows")
        n_label.pack(side=LEFT)
        rows_var = StringVar()
        rows_var.set(20)
        self.n_field = Entry(config_frame, width="3", textvariable=rows_var)
        self.n_field.pack(side=LEFT)
        m_label = Label(config_frame, text="Cols")
        m_label.pack(side=LEFT)
        cols_var = StringVar()
        cols_var.set(20)        
        self.m_field = Entry(config_frame, width="3", textvariable=cols_var)
        self.m_field.pack(side=LEFT)
        self.set_nm_button = Button(config_frame, text="Set dimensions", command=self.set_dimensions)
        self.set_nm_button.pack(side=LEFT)
        self.is_tor = IntVar()
        self.is_tor.set(1)
        is_tor_field = Checkbutton(config_frame, text="Is tor", variable=self.is_tor, command=self.set_tor)
        is_tor_field.pack(side=BOTTOM)
                
        buttons_frame = Frame(sideframe)
        buttons_frame.pack(side=BOTTOM)
        
        self.start_button = Button(buttons_frame, text="Start", command=self.start)
        self.start_button.pack(side=LEFT)
        self.stop_button = Button(buttons_frame, text="Stop", command=self.stop, state=DISABLED)
        self.stop_button.pack(side=LEFT)
        
        self.do_turn_button = Button(buttons_frame, text="Next step", command=self.do_turn)
        self.do_turn_button.pack(side=RIGHT)
        
        self.clear_button = Button(buttons_frame, text="Clear", command=self.clear)
        self.clear_button.pack(side=RIGHT)
        
        generation_label_label = Label(sideframe, text="Generation:")
        generation_label_label.pack(side=LEFT)
        self.generation_label = Label(sideframe, text="0")
        self.generation_label.pack(side=LEFT)
                
        
        self.currtime = ''
        self.run = False
        self.delay = 100
        
        self.desk.rows = 20
        self.desk.cols = 20
        self.desk.draw_grid()
        
        self.game_life = gamelife.GameLife(self.desk.rows, self.desk.cols)
    
    def user_update_cell(self, event):
        if self.run:
            return
        cell = self.desk.get_cell_by_coords(event.x, event.y)
        self.desk.update_cell(cell)
    
    def do_turn(self):        
        matrix = self.game_life.do_turn()
        self.vizualize_turn(matrix)
        self.generation_label.config(text=str(self.game_life.generation))
    
    def timer(self):
        if not self.run:
            return
        newtime = time.strftime('%H:%M:%S')
        if newtime != self.currtime:
            self.currtime = newtime
            self.do_turn()           
        self.start_button.after(self.delay, self.timer)        
        
    def vizualize_turn(self, matrix):
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j]:
                    self.desk.draw_in_cell((i,j))
                else:
                    self.desk.clear_cell((i,j))
    

    def start(self):
        self.start_button.configure(state=DISABLED)
        self.stop_button.configure(state=NORMAL)
        self.set_nm_button.configure(state=DISABLED)
        
        self.game_life = gamelife.GameLife(self.desk.rows, self.desk.cols, self.desk.desk_objects.keys())
        
        self.run = True
        self.timer()

    def stop(self):
        self.start_button.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)
        self.set_nm_button.configure(state=NORMAL)
        self.run = False
        
    def clear(self):
        self.desk.clear_objects()
    
    def set_delay(self):
        try:
            delay = int(self.delay_field.get())
            if delay < 1:
                raise ValueError
        except ValueError:
            tkMessageBox.showinfo(
                "Wrong input",
                "Please specify correct delay"
            )
        else:
            self.delay = delay
    
    def set_dimensions(self):
        try:
            n = int(self.n_field.get())
            m = int(self.m_field.get())
            if n < 1 or n > 100 or m < 1 or m > 100:
                raise ValueError
        except ValueError:
            tkMessageBox.showinfo(
                "Wrong input",
                "Please specify correct dimensions(max 100X100)"
            )
        else:
            self.desk.rows = n
            self.desk.cols = m            
            self.desk.draw_grid()            
            self.game_life = gamelife.GameLife(self.desk.rows, self.desk.cols, self.desk.desk_objects.keys())                    
            self.vizualize_turn(self.game_life.matrix)
    
    def set_tor(self):
        print self.is_tor.get()
        self.game_life.is_tor = self.is_tor.get()
        
root = Tk()
root.title("Python Tkinter implementation of Game of Life, by Taras Bilynskyi")
app = App(root)
root.mainloop()
