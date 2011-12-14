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
        self.changed = copy.deepcopy(self.alive)
        
            
    def do_turn(self):
        
        alive = self.alive #just for performance
        new_alive = copy.deepcopy(self.alive)
        new_changed = set()
        
        for cell in self.changed:
            neighbours = self.calc_neighbours(cell)
            if cell in alive:
                if neighbours < 2 or neighbours < 3:
                    new_alive.discard(cell)
                    new_changed.add(cell)
            else:
                if neighbours == 3:
                    new_alive.add(cell)
                    new_changed.add(cell)
        self.alive = new_alive
        self.changed = new_changed
        self.generation += 1
    
    def calc_neighbours(self, (i,j)):
        neigbour_cells = [
            (i-1,j),
            (i+1,j),
            (i,j-1),
            (i,j+1),
            (i-1,j-1),
            (i+1,j+1),
            (i-1,j+1),
            (i+1,j-1)
        ]
        alive = self.alive
        alive_neighbours = 0
        for cell in neigbour_cells:
            if cell in alive:
                alive_neighbours += 1
        return alive_neighbours

if __name__ == '__main__':
    s = set([1,2,3,4,5])
    for ss in s:
        print ss