import gamelife
import gl

initial_state = []
for i in xrange(100):
    initial_state.append((i,i))
    initial_state.append((i,99-i))

g1 = gamelife.GameLife(100,100, initial_state, False)
g2 = gl.GameLife(100,100, initial_state, False)
for i in xrange(100):
    g1.do_turn()
    g2.do_turn()
    g1alive = g1.set_of_alive()
    g2alive = g2.alive
    if len(g1alive) != len(g2alive):
        print str(i)+' error'