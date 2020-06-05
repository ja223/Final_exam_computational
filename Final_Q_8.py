#Question 8:
#Jagannath Das (DTP.PhD) 
from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt
def y_exact(x):#The Correct solution 
	return np.exp(2)*pow((np.exp(4)-1),-1)*(np.exp(2*x)-np.exp(-2*x))+x
def func(x, y):# The differential equation 
	return np.vstack((y[1], 4*(y[0]-x)))

def boundar_condition(ya, yb):# the boundary values 
	return np.array([ya[0], yb[0]-2])
x=np.linspace(0,1,100)# initial value and final value of x are 0 and 1 respectively. 100 is the numpoints
error=np.zeros(len(x))
y=np.zeros(len(x))
y1= np.zeros((2, x.size))
solution=solve_bvp(func, boundar_condition, x, y1)# boundary value prob by scipy
y_numerical=solution.sol(x)[0]# numerical solution
iteration=[]
for i in range(len(x)):
      y[i]=y_exact(x[i])
      iteration.append(i)
      error[i]=((y_numerical[i]-y[i])*100)/(y[i])# relative percentage error
      print('Number of step:',i+1, 'Relative Error:',error[i])
plt.subplots()
plt.plot(iteration,error,label="Relative percentage error with iteration")
plt.xlabel('iteration')
plt.ylabel('Error in each step')
plt.legend()
plt.subplots()
plt.plot(x,y,'r',label="exact solution of the bounary value problem")
plt.ylabel('y_exact(x)')
plt.xlabel('x')
plt.legend()
plt.subplots()
plt.plot(x,y_numerical,'b',label="numerical solution of the boundary value problem")
plt.ylabel('y_numerical(x)')
plt.xlabel('x')
plt.legend()


plt.show()
