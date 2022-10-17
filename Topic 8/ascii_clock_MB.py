# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Riley Hebert
#               Triston Maresh
#               Malcolm Ferguson
#               Marissa Bosher
# Section:      504
# Assignment:   Topic 8 py file
# Date:         14 October, 2022
#

#have the user input 4 numbers in time format example: "12:30"
time = input('Enter the time: ')
#make input a new list variable 
myList = time.split(":") # .split string method returns a list
#### split the string, putting the substrings for hours and minutes into their own variables ####