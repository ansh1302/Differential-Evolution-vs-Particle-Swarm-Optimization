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

def f2(x):
    """Bent cigar function"""
    sum = 0.0
    sum += x[0]**2
    for i in range(2, len(x)+1):
        sum += x[i-1]**2
    sum *= (10**6)
    return sum

#Function 2
X = np.linspace(-100, 100, 100)            # points from 0..10 in the x axis
Y = np.linspace(-100, 100, 100)            # points from 0..10 in the y axis
X, Y = np.meshgrid(X, Y)               # create meshgrid
Z = f2([X, Y])                         # Calculate Z

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
defiles = ["D2_Ackleys2D_All.csv", "D2_BentCigar2D_All.csv", "D2_DiscusFunc2D_All.csv",
          "D2_Greiwank2D_All.csv", "D2_HighConditioned2D_All.csv", "D2_Katsuura2D_All.csv",
          "D2_Rastrigin2D_All.csv", "D2_Rosenbrock2D_All.csv", "D2_Weierstrass2D_All.csv",
          "D5_Ackleys5D_All.csv", "D5_BentCigar5D_All.csv", "D5_DiscusFunc5D_All.csv",
           "D5_Greiwank5D_All.csv", "D5_HighConditioned5D_All.csv", "D5_Katsuura5D_All.csv",
           "D5_Rastrigin5D_All.csv", "D5_Rosenbrock5D_All.csv", "D5_Weierstrass5D_All.csv",
           "D10_Ackleys10D_All.csv", "D10_BentCigar10D_All.csv", "D10_DiscusFunc10D_All.csv",
           "D10_Greiwank10D_All.csv", "D10_HighConditioned10D_All.csv", "D10_Katsuura10D_All.csv",
           "D10_Rastrigin10D_All.csv", "D10_Rosenbrock10D_All.csv"]

psfiles = ["PSO_2D_Ackleys_PSO_ALL.csv", "PSO_2D_BentCigar_PSO_ALL.csv", "PSO_2D_Discus_PSO_ALL.csv",
          "PSO_2D_Griewanks_PSO_ALL.csv", "PSO_2D_HighConditioned_PSO_ALL.csv", "PSO_2D_Katsuura_PSO_ALL.csv",
          "PSO_2D_Rastrigins_PSO_ALL.csv", "PSO_2D_Rosenbrocks_PSO_ALL.csv", "PSO_2D_Weierstrass_PSO_ALL.csv",
          "PSO_5D_Ackleys_PSO_ALL.csv", "PSO_5D_BentCigar_PSO_ALL.csv", "PSO_5D_Discus_PSO_ALL.csv",
           "PSO_5D_Griewanks_PSO_ALL.csv", "PSO_5D_HighConditioned_PSO_ALL.csv", "PSO_5D_Katsuura_PSO_ALL.csv",
           "PSO_5D_Rastrigins_PSO_ALL.csv", "PSO_5D_Rosenbrocks_PSO_ALL.csv", "PSO_5D_Weierstrass_PSO_ALL.csv",
           "PSO_10D_Ackleys_PSO_ALL.csv", "PSO_10D_BentCigar_PSO_ALL.csv", "PSO_10D_Discus_PSO_ALL.csv",
           "PSO_10D_Griewanks_PSO_ALL.csv", "PSO_10D_HighConditioned_PSO_ALL.csv", "PSO_10D_Katsuura_PSO_ALL.csv",
           "PSO_10D_Rastrigins_PSO_ALL.csv", "PSO_10D_Rosenbrocks_PSO_ALL.csv"]

ax.plot_surface(X, Y, Z,
                            rstride=3,
                            cstride=3,
                            alpha=0.3,
                            cmap='hot')

wholeCount = 0
while (wholeCount < 26):
    with open(psfiles[wholeCount]) as f:
        cf = csv.reader(f)
        with open(defiles[wholeCount]) as g:
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
    wholeCount += 1
plt.show(block=True)