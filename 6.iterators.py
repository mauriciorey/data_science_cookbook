class SimpleCounter(object):
    "Iterator"
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        "Returns itself as an iterator object"
        return self
    
    def next(self):
        "Returns the next value until current is lower than end"
        if self.current > self.end:
        
            raise StopIteration
        else:
        	self.current += 1
        	return self.current - 1

c = SimpleCounter(1,3)

print c.next()
print c.next()
print c.next()

#Another way to access the entries
for entry in iter(c):
    print entry
