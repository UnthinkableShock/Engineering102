# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Riley Hebert
#               Triston Maresh
#               Malcolm Ferguson
#               Marissa Bosher
# Section:      504
# Assignment:   Topic 12 matplotlib example
# Date:         14 November, 2022
#

# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material 


import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100) #np.linspace(start, end, length), generates a 1D array of x values to use

def equation(x, f):
    return (1/4)/f*x**2

fig, ax = plt.subplots() # weird python unpacking thingy
f = 2
ax.plot(x, equation(x, f), c='r', lw=f, label=f'f={f}')
# c is shorthand for color, which would also work
# lw is shorthand for linewidth, which would also work
# label= defines the label, have to give it a string
f = 6
ax.plot(x, equation(x, f), c='b', lw=f, label=f'f={f}')
ax.legend() # adds any labels defined

x2 = np.linspace(-4, 4, 25) # generates a 1D array of x values to use
def y(x):
    return 2*x**3 + 3*x**2 - 11*x - 6
fig2, ax2 = plt.subplots()
ax2.plot(x2, y(x2), '*', markersize=10, markerfacecolor=(1, 1, 0, 1), markeredgecolor='k')


x3 = np.linspace(-6, 6, 100)
fig3, (ax3, ax4) = plt.subplots(2, 1) # 2, 1 = 2 rows, 1 column
ax3.set_title("Plot of cos(x) and sin(x)")
ax3.plot(x3, np.cos(x3), c='r', label='cos(x)')
ax4.plot(x3, np.sin(x3), c='b', label='sin(x)')
ax3.legend()
ax4.legend()