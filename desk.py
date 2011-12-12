from Tkinter import *

class Desk(Canvas):
    
    def __init__(self, rows=10, cols=10, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        
        self.rows = rows
        self.cols = cols
        self.padding = 1
        
        self.grid_lines = []
        self.desk_objects = {}
        
        self.draw_grid()
        
    def draw_grid(self):
        self.clear_desk()
        self.desk_width = int(self.cget("width"))
        self.desk_height = int(self.cget("height"))        
        self.cell_size = min(self.desk_width/self.rows, self.desk_height/self.cols)
        self.padding = int(self.cell_size / 10) 
        for i in xrange(1, self.rows):
            self.grid_lines.append(self.create_line(0, i*self.cell_size, self.desk_width, i*self.cell_size))
        for i in xrange(1, self.cols):
            self.grid_lines.append(self.create_line(i*self.cell_size, 0, i*self.cell_size, self.desk_height))
    
    def clear_desk(self):
        self.clear_grid()
        self.clear_objects()
    
    def clear_grid(self):
        for line in self.grid_lines:
            self.delete(line)
        self.grid_lines = []
    
    def clear_objects(self):
        for k in self.desk_objects.keys():
            self.delete(self.desk_objects[k])
        self.desk_objects = {}
        
    def get_cell_by_coords(self, x, y):
        j = x / self.cell_size
        i = y / self.cell_size
        return (i,j)
    
    def draw_object_by_coords(self, x, y):
        cell = self.get_cell_by_coords(x, y)
        return self.draw_in_cell(cell)
    
    def draw_in_cell(self, cell):
        if cell not in self.desk_objects.keys():
            self.desk_objects[cell] = self.create_rectangle(
                    cell[1]*self.cell_size+self.padding, cell[0]*self.cell_size+self.padding, 
                    (cell[1]+1)*self.cell_size-self.padding, (cell[0]+1)*self.cell_size-self.padding, 
                    fill="#ff0000"
            )
            return True
        return False
    
    def clear_cell(self, cell):
        if cell in self.desk_objects.keys():
            self.delete(self.desk_objects[cell])
            del self.desk_objects[cell]
    
    def update_cell(self, cell):
        if not self.draw_in_cell(cell):
            self.clear_cell(cell)
            