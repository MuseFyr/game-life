import gamelife
import gl
import time
initial_state = []
for i in xrange(100):
    initial_state.append((i,i))
    initial_state.append((i,99-i))
initial_state.append((4,5))
initial_state.append((5,5))
initial_state.append((5,4))
initial_state.append((4,4))

#initial_state = [(2,1),(2,2),(2,0)]
#initial_state = [(0,1),(0,2),(0,3),(0,4)]

n=100
m=100

is_tor = False

g1 = gamelife.GameLife(n,m, initial_state, is_tor)
g2 = gl.GameLife(n,m, initial_state, is_tor)

iter_num = 100

print 'start'
start_time = time.time()
for i in xrange(iter_num):
    g1.do_turn()
slow =  time.time() - start_time

start_time = time.time()
for i in xrange(iter_num):
    g2.do_turn()
fast =  time.time() - start_time

if g1.set_of_alive() <= g2.alive and g1.set_of_alive() >= g2.alive:
    print 'tested OK'
else:
    print 'tested Failed'

print 'slow = '+str(slow)
print 'fast = '+str(fast)


#
#g1alive = g1.set_of_alive()
#g2alive = g2.alive
#if len(g1alive) != len(g2alive):
#    print str(i)+' error:'
#    
#else:
#    print 'init ok'
#g1._print()
#g2.print_matrix()
#print '========================='
#
#done = True
#
#for i in xrange(1000):
#    g1.do_turn()
#    g2.do_turn()
#    g1alive = g1.set_of_alive()
#    g2alive = g2.alive
#    len_g1alive = len(g1alive)
#    len_g2alive = len(g2alive)
#    g1._print()
#    g2.print_matrix()
#    print '========================='
#    if len_g1alive != len_g2alive:
#        done = False
#        print str(i+1)+' error: '+str(len_g1alive)+' vs '+str(len_g2alive)
#        print '  '+str(g1alive)
#        print '  '+str(g2alive)
#        print ''
#if done:
#    print 'PASS'
#else:
#    print 'FAILED'