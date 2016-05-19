
print zip(range(1,10,2), range(2,20,4))

# Unpacking lists
a = (2,3)
print pow(*a)

# Unpacking Dicts

dictionary = {'x': 10, 'y': 10, 'z': 10, 'x1': 10, 'y1': 10, 'z1': 10}

def dist(x,y,z,x1,y1,z1):
    return abs((x-x1) + (y-y1) + (z-z1))

print dist(**dictionary)

def any_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print any_sum(1,2,3,4,5,6,7,8,9,1,2,3,4)
