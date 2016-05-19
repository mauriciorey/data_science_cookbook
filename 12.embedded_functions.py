#Embedded functions
def sum_squares(x):
    def square_input(x):
        return x*x
    return sum([square_input(value) for value in x])

print sum_squares([1,2,3,5,6,7,8,9,10])

#Passing a function as a parameter

from math import log

def input_square(x):
    return x*x

def apply_func(func_x, input_x):
    return map(func_x, input_x)
    
a = [2,4,6]

print apply_func(input_square, a)
print apply_func(log, a)
