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
#from ascii_clock_RH import myNumbers
#have the user input 4 numbers in time format example: "12:30"
fromascii_clock_MB import time


myList = time.split(":") # .split string method returns a list

newTime = []
for x in range(len(time)):
    if time[x] != ":":
        newTime.append(int(time[x]))
#print(newTime)
one = myNumbers[newTime[0]]
two = myNumbers[newTime[1]]
seporator = myNumbers[10]
three = myNumbers[newTime[2]]
four = myNumbers[newTime[3]]

print()
if newTime[0] == 0:
    for x in range(len(myNumbers[0])): print(two[x],seporator[x], three[x], four[x])
else:
    for x in range(len(myNumbers[0])): print(one[x], two[x],seporator[x], three[x], four[x])
