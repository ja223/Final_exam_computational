#Question 6
#Jagannath Das(DTP)(PhD)
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def f1(x,y1,y2):# The given equations
    return (32*y1+66*y2+(2/3)*x+(2/3))
def f2(x,y1,y2):
    return (-66*y1-133*y2-(1/3)*x-(1/3))
h=0.001 #the step size
a=0 # initial value of x
b=0.5 # final value of x
n=int((b-a)/h)
x=np.linspace(a,b,n+1)
def diff(z,x):#definition of z to solve the initial value prob by scipy.integrate odeint
    dy1dx=32*z[0]+66*z[1]+(2/3)*x+(2/3)
    dy2dx=-66*z[0]-133*z[1]-(1/3)*x-(1/3)
    dzdx=[dy1dx,dy2dx]
    return dzdx
z_initial=[1/3,1/3]
z=odeint(diff,z_initial,x)# solution by scipy.integrate odeint
y1 = np.zeros((n+1,)) 
y2 = np.zeros((n+1,)) 
x[0]=0
y1[0]=(1/3)
y2[0]=(1/3)
for i in range(1,n+1): # The formula for Runge Kutta fourth order for ODE
    k11=h*f1(x[i-1],y1[i-1],y2[i-1])
    k12=h*f2(x[i-1],y1[i-1],y2[i-1])
    k21=h*f1(x[i-1]+h/2,y1[i-1]+k11/2,y2[i-1]+k12/2)
    k22=h*f2(x[i-1]+h/2,y1[i-1]+k11/2,y2[i-1]+k12/2)
    k31=h*f1(x[i-1]+h/2,y1[i-1]+k21/2,y2[i-1]+k22/2)
    k32=h*f2(x[i-1]+h/2,y1[i-1]+k21/2,y2[i-1]+k22/2)
    k41=h*f1(x[i-1]+h,y1[i-1]+k31,y2[i-1]+k32)
    k42=h*f2(x[i-1]+h,y1[i-1]+k31,y2[i-1]+k32)
    y1[i] = y1[i-1]+(k11+2*k21+2*k31+k41)*(1/6)
    y2[i] =y2[i-1]+(k12+2*k22+2*k32+k42)*(1/6)
    
y1_real=z[:,0]
y2_real=z[:,1]
error_1=np.zeros(len(x))
error_2=np.zeros(len(x))
for i in range(len(x)):
       error_1[i]=(y1[i]-y1_real[i])/y1_real[i]
       error_2[i]=(y2[i]-y2_real[i])/y2_real[i]
       print('Relative Error for y1:',error_1[i])
       print('Relative Error for y2:',error_2[i])
plot1 = plt.figure(1)
plt.plot(x,z[:,0],'r',label="Solution y1  of the initial value prob by odeint")
plt.plot(x,y1,'b', label="Solution y1  of the initial value prob by Runge Kutta fourth order")

plt.xlabel('x')
plt.ylabel('y1(x)')
plt.grid()
plt.legend()

plot2 = plt.figure(2)
plt.plot(x,z[:,1],'r',label="Solution y1  of the initial value prob by odeint")
plt.plot(x,y2,'b',label="Solution y1  of the initial value prob by Runge Kutta fourth order")

plt.xlabel('x')
plt.ylabel('y2(x)')
plt.grid()
plt.legend()


plt.show()
