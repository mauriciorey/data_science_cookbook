#Embedded functions
def sum_squares(x):
    def square_input(x):
        return x*x
    return sum([square_input(value) for value in x])

print sum_squares([1,2,3,5,6,7,8,9,10])