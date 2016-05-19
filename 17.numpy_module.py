import numpy as np

a_list = [1,2,3,4,5]

an_array = np.array(a_list, dtype = float)

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

a_matrix = np.matrix(list_of_lists, dtype = float)

def display_shape(a):
    print(a.size)
    print(a.ndim)

display_shape(a_matrix)

created_array = np.arange(1,10, dtype = float)
display_shape(created_array)

created_array = np.linspace(1,10)
display_shape(created_array)

created_array = np.logspace(1,10, base = 10.0)
display_shape(created_array)

#Matrix with all elements as 1
one_matrix = np.ones((3,3))
print one_matrix

#Matrix with all elements as zeros
zero_matrix = np.zeros((3,3))
print zero_matrix

#Identity matrix
identity_matrix = np.eye(N=3, M=3, k=0)
print identity_matrix

other_identity_matrix = np.eye(N=3, k=1)
print other_identity_matrix

back_to_array = a_matrix.reshape(-1)
print back_to_array

a_matrix = np.arange(9).reshape(3,3)
back_array = np.ravel(a_matrix)
print back_array

a_matrix = np.arange(9).reshape(3,3)
b_matrix = np.arange(9).reshape(3,3)
back_array = a_matrix.flatten()
print back_array

c_matrix = a_matrix + b_matrix
print c_matrix

d_matrix = a_matrix * b_matrix
print d_matrix

e_matrix = np.dot(a_matrix, b_matrix)
print e_matrix

f_matrix = e_matrix.T
print f_matrix

#Grid commands
xx,yy,zz = np.mgrid[0:3,0:3,0:3]
xx = xx.flatten()
yy = yy.flatten()
zz = zz.flatten()

print xx
print yy
print zz
