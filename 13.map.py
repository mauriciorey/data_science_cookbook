# Working with maps
a = [10,20,30]

print map(lambda x: x**2, a)
print sum(map(lambda x: x**3, a))

b = [1,2,3]

print map(pow, a, b)

# Working with filters
print filter(lambda x: x > 15, a)
