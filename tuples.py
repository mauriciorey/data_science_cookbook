# Operations allowed with Tuples: "in" and "not in", comparison, concat, slicing, indexing and mix() max()

tuple1 = (1,2,'a')
tuple2 = 1,2,'c'

print tuple1[0]
print tuple2[-1]

tuple3 = (1,2,[10,20,30])
tuple3[2][0] = 100
print tuple3
print min(tuple1)


if 1 in tuple3:
    print "good"
else:
    print "nothing"

# Calculating Manhattan Distance
from collections import namedtuple

vector = namedtuple('Dimension', 'x,y,z')
vec1 = vector(1,1,1)
vec2 = vector(1,0,1)

distance = abs(vec1.x - vec2.x) + abs(vec1.y - vec2.y) + abs(vec1.z - vec1.z)

print 'Manhattan distance is %d' %(distance)