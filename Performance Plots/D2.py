from numpy import genfromtxt
import matplotlib.pyplot as plt

per_data=genfromtxt('2D_Griewanks_PSO.csv',delimiter=',')
plt.plot(per_data)
plt.xlabel('# of Generation')
plt.ylabel('Best Fitness')
plt.show()