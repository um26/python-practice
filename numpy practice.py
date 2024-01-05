import numpy as np

a= np.array([[2.1,5.0,8.0],[3.0,4.0,7.0]])
print(a)

#get a specific element
print(a[1,2]) #similarily you can get a certain row/column and you can even update an element 

#[start_index:end_index:step_size]
print(a[0:-1:1])

b=np.array([[[3.4,2.6,2.5,2.4],[2.4,3.1,6.4,3.9]],[[3.2,4.3,1.6,5.4],[2.6,8.5,7.2,9.5]]])
print(b)

c=np.ones((2,4,5)) #for 0 and 1 matrices we can use like this
print(c)

d=np.full((4,2,3), 54)#any other number
print(d)

e=np.random.rand(4,2) #generate random numbers, for integer entries use randint insted of just rand
print(e)

f=np.identity(7)#generates identity matrix
print(f)

f=np.repeat([[1,2,3]],3,axis=0) #repeat elements, try with axis 1 as well
print(f)

spl_matrix=np.ones((5,5)) ##program to create a special matrix 
z=np.zeros((3,3))
z[1,1]=9
spl_matrix[1:-1,1:-1]=z
print(spl_matrix)

z=np.array([1,2,3,4,5])#some mathematics with array
print(z+2)
print(z*2)
print(z**2)
print(np.cos(z))

p=np.ones((3,3))
q=np.full((3,3),4)
print(np.matmul(p,q)) #matrix multiplication 
print(np.linalg.det(p))#determinant of matrix
print(np.linalg.eig(p))#eigenvalue

print(np.min(a))## can be used for statistics such as min,max,sum
print(np.sum(a))

before=np.array([[1,2,3,4],[3,4,5,1]]) #can be used to reorganize array
print(before)
after=before.reshape((4,2))
print(after)
print(np.vstack([before[0,:],before[1,:],before[1,:],before[0,:]]))