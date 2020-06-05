#Question 9
#Jagannath Das
import numpy as np
A=[[2,1],[1,0],[0,1]]# first matrix
B=[[1,1,0],[1,0,1],[0,1,1]]# second matrix
U1,S1,V1=np.linalg.svd(A) # SVD solution by numpy
U2,S2,V2=np.linalg.svd(B)
print(' singular values of matrix 1:')
print(S1)
print('singular values of matrix 2:')
print(S2)
