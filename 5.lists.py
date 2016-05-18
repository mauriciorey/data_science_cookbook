lista = range(1,20)
print lista

from random import shuffle

shuffle(lista)
print lista

lista.sort()
print lista

lista.reverse()
print lista

#List comprehension
a = [1,2,-1,-2,3,4,-3,-4]
b = [pow(x,2) for x in a if x < 0]
print b

#Dict comprehension
c = {'a':1,'b':2,'c':3}
d = {x:pow(y,2) for x,y in c.items()}
print d

#Tuple comprehension

def process(x):
    if isinstance(x,str):
        return x.lower()
    elif isinstance(x,int):
        return x*x
    else:
        return -9

a = (1,2,-1,-2,'D',3,4,-3,'A')
b = tuple(process(s) for s in a)
print b
