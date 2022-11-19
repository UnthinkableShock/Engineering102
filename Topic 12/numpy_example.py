# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Riley Hebert
#               Triston Maresh
#               Malcolm Ferguson
#               Marissa Bosher
# Section:      504
# Assignment:   Topic 12 numpy example
# Date:         14 November, 2022
#

# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material 

import numpy as giraffe

# important commands
# np.array
# arange
# .shape
# .reshape
# limspace
# size
# array
# @ is matrix multiplication
# .transpose()

A = giraffe.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]) # needs to be 3 x 4
B = giraffe.array([[0, 1], [2, 3], [4, 5], [6, 7]]) # needs to be 4 x 2
C = giraffe.array([[0, 1, 2], [3, 4, 5]]) # needs to be 2 x 3

D = A @ B @ C
TD = D.transpose()
E = D**(1/2) / 2

print(f"A = {A}\n\nB = {B}\n\nC = {C}\n\nD = {D}\n\nD^T = {TD}\n\nE = {E}")