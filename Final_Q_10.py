#Question 10
# Jagannath Das
import numpy as np
import matplotlib.pyplot as plt
def func(x):#Definition of the function
    if abs(x)<=1:
        value=1
    else:
        value=0
    return value
def DFT(func_arr):# Definition of the DFT
    N = len(func_arr)
    Fourier_arr = []
    for m in range(N):
        F = 0
        for n in range(N):
            F += func_arr[n] * np.exp(- 2j *np.pi * m * n / N)
        Fourier_arr.append(F / (np.sqrt(N)))
    return Fourier_arr
x_ar=np.zeros(100)
func_ar=np.zeros(100)
x_low=-5
x_high=+5
dx=((x_high-x_low)/99)
x_ar[0]=-5
for i in range(100):
           x_ar[i] = x_low+i*dx
           func_ar[i] = func(x_ar[i])
def fourier(N):
    x_min = -10.0 #minimum value of x
    x_max = 10.0#maximum value of x
    numpoints = N #number of sample points
    delta = (x_max-x_min)/(numpoints-1)# resolution
    func_arr = np.zeros(numpoints,)
    x_arr = np.zeros(numpoints)
    for i in range(numpoints):
           x_arr[i] = x_min+i*delta
           func_arr[i] = func(x_arr[i])
    nft =  DFT(func_arr)# Discrete fourier transform of the function
    karr =2*np.pi* np.fft.fftfreq(numpoints, d=delta)# k points 
    factor = np.exp(-1j * karr * x_min)
    aft = delta * np.sqrt(numpoints/(2.0*np.pi)) * factor * nft # Definition of fourier transform fron discrete fourier trnsform 
    return np.array([karr,aft])
plt.subplots()
plt.plot(x_ar,func_ar,'b',label='The Box function ')
plt.title('The Box function')
plt.xlabel('x',fontsize=16)
plt.ylabel('func_x',fontsize=16)
plt.grid(True)

plt.subplots()
plt.plot(fourier(1024)[0],fourier(1024)[1],'b', label='The fourier transform of the box function for sampling rate (100/2023)')
plt.xlabel('k',fontsize=16)
plt.ylabel('Fourier_f',fontsize=16)
plt.grid(True)
plt.legend()
plt.subplots()
plt.plot(fourier(128)[0],fourier(128)[1],'g', label='The fourier transform of the box function for sampling rate (100/127)')
plt.xlabel('k',fontsize=16)
plt.ylabel('Fourier_f',fontsize=16)
plt.grid(True)
plt.legend()
plt.subplots()
plt.plot(fourier(512)[0],fourier(512)[1],'r', label='The fourier transform of the box function for sampling rate (100/511)')
plt.title('The fourier transform of the box function')
plt.xlabel('k',fontsize=16)
plt.ylabel('Fourier_f',fontsize=16)
plt.grid(True)
plt.legend()
plt.show()
