import copy

class GameLife:
    
    def __init__(self, rows=20, cols=20, initial_state=None, is_tor=False):
        self.rows = rows
        self.cols = cols
        self.is_tor = is_tor
        self.generation = 0
        if initial_state is None:
            self.alive = set()
        else:
            self.alive = set(initial_state)
        self.changed = set()
        for cell in self.alive:
            self.changed.update(self.get_neighbours(cell))
        
            
    def do_turn(self):
        
        alive = self.alive #just for performance
        new_alive = copy.deepcopy(self.alive)
        new_changed = set()
        
        for cell in self.changed:
            neighbours = self.calc_neighbours(cell)
            if cell in alive:
                if neighbours < 2 or neighbours > 3:
                    new_alive.discard(cell)
                    new_changed.update(self.get_neighbours(cell))
            else:
                if neighbours == 3:
                    new_alive.add(cell)
                    new_changed.update(self.get_neighbours(cell))
        self.alive = new_alive
        self.changed = new_changed
        self.generation += 1
    
    def get_neighbours(self, (i,j)):
        neighbours = [
            (i-1,j),
            (i+1,j),
            (i,j-1),
            (i,j+1),
            (i-1,j-1),
            (i+1,j+1),
            (i-1,j+1),
            (i+1,j-1)
        ]
        result = set()
        for (x,y) in neighbours:            
            if self.is_tor:
                xx = x
                yy = y
                if x < 0:
                    xx = self.rows+x
                if y < 0:
                    yy = self.cols+y
                if x >= self.rows:
                    xx = x-self.rows
                if y >= self.cols:
                    yy = y-self.cols
                result.add((xx,yy))
            else:
                if x >= 0 and y >= 0 and x < self.rows and y < self.cols:
                    result.add((x,y))
                        
        return result
    
    def calc_neighbours(self, (i,j)):
        neigbour_cells = self.get_neighbours((i, j))
        alive = self.alive#just for performance
        alive_neighbours = 0
        for cell in neigbour_cells:
            if cell in alive:
                alive_neighbours += 1
        return alive_neighbours
    
    def print_matrix(self):
        for i in xrange(self.rows):
            str = ''
            for j in xrange(self.cols):
                if (i,j) in self.alive:
                    str += '#'
                else:
                    str += '-'
            print str

if __name__ == '__main__':
    initial_state = [(3,1),(3,2),(3,3)]

    g1 = GameLife(6,5, initial_state, False)
    g1.print_matrix()
    print ''
    g1.do_turn()
    g1.print_matrix()
    print ''
    
    g1.do_turn()
    g1.print_matrix()
    print ''
    
    g1.do_turn()
    g1.print_matrix()
    print ''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    