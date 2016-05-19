class SimpleIterable(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        for x in range(self.start, self.end):
            yield x**2

c = SimpleIterable(1,10)

#First iteration
tot = 0
for val in iter(c):
    tot += val
print tot

#Second iteration and doesn't raise any exception
tot = 0
for val in iter(c):
    tot += val
print tot
