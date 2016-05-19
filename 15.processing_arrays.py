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

#Preprocessing columns
in_data = StringIO("30kg,inr2000,31.11,56.33,1\n52kg,inr8000.35,12,16.7,2")

strip_func_1 = lambda x: float(x.rstrip('kg'))
strip_func_2 = lambda x: float(x.lstrip('inr'))

convert_funcs = {0:strip_func_1, 1:strip_func_2}
data = np.genfromtxt(in_data, delimiter = ',', converters = convert_funcs)
print data
