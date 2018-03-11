from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from csv import reader
import matplotlib.pyplot as plt
import numpy as np
import csv
from random import randint
import time
from random import random, seed
from mpl_toolkits.mplot3d import *
from matplotlib import cm

def f9(x):
    """Katsuura Function"""
    product = 1
    for i in range(0, len(x)):
        sum = 0
        for j in range(1,33):
            term = np.power(2,j) * x[i]
            sum += np.abs(term - np.round(term))/(np.power(2,j))
        product *= np.power(1+((i+1)*sum),10.0/ np.power(len(x),1.2))
    return (10/len(x) * len(x) * product - (10/len(x) * len(x)))

#Function 9
X = np.linspace(-10, 10)            # points from 0..10 in the x axis
Y = np.linspace(-10, 10)            # points from 0..10 in the y axis
X, Y = np.meshgrid(X, Y)               # create meshgrid
Z = f9([X, Y])                         # Calculate Z

plt.ion()
# Plot the 3D surface for first function from project
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []
a = []
b = []
c = []

ax.plot_surface(X, Y, Z,
                            rstride=3,
                            cstride=3,
                            alpha=0.3,
                            cmap='hot')

with open('PSO_2D_Ackleys_PSO_ALL.csv') as f:
    cf = csv.reader(f)
    with open('D2_Ackleys2D_All.csv') as g:
        cg = csv.reader(g)
        count = 1
        count2 = 1
        for row in cf:
            for row2 in cg:
                a.append(float(row2[0]) * 10)
                b.append(float(row2[1]) * 10)
                c.append(float(row2[2]) * 10)
                if ((count2%100) == 0):
                    break
                count2 += 1
            x.append(float(row[0])*10)
            y.append(float(row[1])*10)
            z.append(float(row[2])*10)
            print count
            if ((count%100) == 0):
                if (count > 100):
                    px.remove()
                    px2.remove()
                px = ax.scatter(x, y, z, c='r', marker='o')
                px2 = ax.scatter(a, b, c, c='b', marker='o')

                ax.set_xlabel('Gene 1')
                ax.set_ylabel('Gene 2')
                ax.set_zlabel('Fitness Value')

                fig.canvas.draw()

                x = []
                y = []
                z = []
                a = []
                b = []
                c = []
                #plt.show()
                #count = 0
            count += 1