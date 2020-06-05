#Question 4
#Jagannath Das
import numpy as np 
import matplotlib.pyplot as plt 
import math
N=1024 # the number of random number to be generated
random_number= np.random.rand(N) ##random nos
plt.subplots()
plt.plot(random_number, "g.", label = "rand_sample")
plt.grid(True)
plt.xlabel('index')
plt.ylabel('sample_data')
plt.legend()
rand_dft=np.fft.fft(random_number,norm='ortho')#Discrete Fourier Transform by numpy
frequency=np.fft.fftfreq(N,d=1)# k points 
freq=2*np.pi*frequency
Power_spec=np.zeros(len(freq))
for i in range(len(freq)):# definition of power spectrum
	Power_spec[i]=(1/N)*abs(rand_dft[i])**2
plt.subplots()
plt.plot(freq,Power_spec, "c", label = "Power spectra using periodogram")
plt.grid(True)
plt.xlabel('K')
plt.ylabel('Power spectra')
plt.legend()
print("Minimum value of k is: ", min(freq))
print("Maximum value of k is: ", max(freq))
bins=5
plt.subplots()
plt.hist(Power_spec,range=(min(freq),max(freq)),bins=5,density='true',color="maroon",label='Histogram')
plt.xlabel(r'$bins$',fontsize=16)
plt.ylabel('Binned power spectra',fontsize=16)
plt.legend()
plt.show()
