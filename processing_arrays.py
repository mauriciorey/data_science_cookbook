import numpy as np
from StringIO import StringIO

in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype = int, delimiter = ',')

#When in want to use certain columns
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data1 = np.genfromtxt(in_data, dtype = int, delimiter = ',', usecols = (0,1))

#Providing column names
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data2 = np.genfromtxt(in_data, dtype = int, delimiter = ',', names = 'a,b,c')

#using column names from data
in_data1 = StringIO("a,b,c\n10,20,30\n56,89,90\n33,46,89")
data3 = np.genfromtxt(in_data1, dtype = int, delimiter = ',', names = True)

print data
print data1
print data2
print data3 