import copy

class GameLife:
    
    def __init__(self, N, M, filled=None, is_tor=True):
        self.N = N
        self.M = M
        self.generation = 0
        self.is_tor = is_tor
        
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
        self.generation += 1
        return copy.deepcopy(self.matrix)
    
    def _pos(self, (i, j), matrix):
        if self.is_tor:
            ii = i
            jj = j
            if i >= self.N:
                ii = i-self.N
            if j >= self.M:
                jj = j-self.M
            return matrix[ii][jj]                
        else:
            if i < 0 or j < 0 or i >= self.N or j >= self.M:
                return None
            else:
                return matrix[i][j]

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
                    line += '#'
                else:
                    line += '-'
            print line
        print ''
        
    def set_of_alive(self):
        res = set()
        for i in xrange(self.N):
            for j in xrange(self.M):
                if self.matrix[i][j]:
                   res.add((i,j))
        return res 
                    
if __name__ == '__main__':
    game = GameLife(5,7,[
                         (2,2),(2,3),(2,4)
                         ])
#    game._print()
#    game.do_turn()
#    game._print()
    
    def pos((i,j), matrix, n,m, is_tor):
        if is_tor:
            ii = i
            jj = j
            if i >= n:
                ii = i-n
            if j >= m:
                jj = j-m
            return matrix[ii][jj]                
        else:
            if i < 0 or j < 0 or i >= n or j >= m:
                print 'NOT tor NOT in range'
                return None
            else:
                print 'NOT tor in range'
                return matrix[i][j]
    matrix1 = [
              [1,2,3],
              [4,5,6],
              [7,8,9]              
              ]
    print pos((-1,2), matrix1, 3,3, False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    