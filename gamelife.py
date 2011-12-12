import copy

class GameLife:
    
    def __init__(self, N, M, filled=None):
        self.N = N
        self.M = M
        
        self.matrix = []
        for i in xrange(self.N):
            self.matrix.append([])
            for j in xrange(self.M):
                self.matrix[i].append(False)
        if filled:
            for f in filled:
                self.matrix[f[0]][f[1]] = True
    
    def do_turn(self):
        tmp_matrix = copy.deepcopy(self.matrix)
        for i in xrange(self.N):
            for j in xrange(self.M):
                neigh_num = 0
                for point in self._go_around(i,j):
                    if self._pos(point, tmp_matrix):
                        neigh_num += 1
                if tmp_matrix[i][j]:
                    if neigh_num == 0 or neigh_num == 1 or neigh_num >= 4:
                        self.matrix[i][j] = False
                else:
                    if neigh_num == 3:
                        self.matrix[i][j] = True
        return copy.deepcopy(self.matrix)
    
    def _pos(self, (x, y), matrix):
        try:
            r = matrix[x][y]
        except IndexError:
            return None
        return r

    def _go_around(self, x,y):
        return [
            (x-1,y),
            (x+1,y),
            (x,y-1),
            (x,y+1),
            (x-1,y-1),
            (x+1,y+1),
            (x-1,y+1),
            (x+1,y-1)
        ]
    def _print(self):
        for row in self.matrix:
            line = ''
            for col in row:
                if col:
                    line += '*'
                else:
                    line += '-'
            print line
        print ''
                    
if __name__ == '__main__':
    game = GameLife(5,7,[
                         (2,2),(2,3),(2,4)
                         ])
    game._print()
    game.do_turn()
    game._print()