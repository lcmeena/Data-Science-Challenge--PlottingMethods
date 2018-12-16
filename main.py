# -*- coding: utf-8 -*-
"""
CarminePanther
9-17-18
Challenge 1

"""
import numpy as np
import matplotlib.pyplot as mplot

#reads file, splits by line
file=open("FreqInfo.csv", "r")
data=file.read()
data=data.replace(" ", "")
data=data.split("\n")

#the 3 lists that i use throughout the file
xaxis=[]
yaxis=[]
amplitude=[]

"""
reads FreqInfo file, turns the strings into
number values, and filters out the unnessecary frequencies
"""
for i in range(0,len(data)-1):
    data[i]=data[i].split(",")
    data[i][0]= np.float64(data[i][0])
    data[i][1]= np.float64(data[i][1])
    data[i][2]= np.float64(data[i][2])
    if data[i][2]>60.00:
        xaxis.append(data[i][0])
        yaxis.append(data[i][1])
        


for i in range(0, len(xaxis)): 
    if i==0 or xaxis[i] != xaxis[i-1]:          #for loop finds start time
        k = i                                   #used k so i wouldn't change
        index=0
        ampsum=0
        mean=0
        while k != len(xaxis)-1 and xaxis[k] == xaxis[k+1]:     
            ampsum += yaxis[k]      #while loop runs until time changes
            index+=1            
            k += 1
        mean = ampsum/index         #calculation finds mean
        amplitude.append(mean)      #adds mean to amplitude list
        
list1=list(set(xaxis))      #creates a list that creates time intervals
list1.sort()                #sorts time

mplot.plot(list1, amplitude, c="red")        #plot line


mplot.scatter(xaxis,yaxis)     #scatterplot. xaxis and yaxis are not labeled yet
     
mplot.xlabel("time(milliseconds)")           #labels x axis
mplot.ylabel("amplitude")                   #labels y axis
mplot.title("frequency")

mplot.show()

