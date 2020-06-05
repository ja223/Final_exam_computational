#Question 7
#Jagannath Das
import numpy as np
import matplotlib.pyplot as plt
import time
n=10000
def func(Random,X0):
    i=0
    while(i<len(Random)):
        if (Random[i]==X0):
            print(X0, "is found again  in the array of random number at",i)
            break
        i=i+1
    else:
        print(X0,"is not found anywhere")
    return " "

########################################################Example of linear conguential generator when seed retuns again
a = 7 #multiplier
c = 7# increment
m = 10 #modulus
x0 = 7#seed
x=7

rand_numbers = []
for i in range(n):#formula of linear congruential Random generator
    x  = (a*x + c)%m
    rand_numbers.append(x)
func(rand_numbers,x0)
########################################################Example of linear conguential generator when seed never retun again
a1=1664525 #multiplier
c1=1013904223# increment
m1=4294967296#modulus
x1=1
x01=x1#seed
rand_numbers1 = []
for i in range(n):
    x1  = (a1*x1 + c)%m1
    rand_numbers1.append(x1)
func(rand_numbers1,x01)
