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

#### get input and store it into a variable ####
#have the user input 4 numbers in time format example: "12:30"
#make input a new list variable 
time = input('Enter the time: ')
if len(time)<5:
    time = "0"+time
myList = time.split(":") # .split string method returns a list

#### put the resulting strings for hours and minutes into their own variables ####
hours = myList[0]
minutes = myList[1]

#### define the structure for the numbers ####
myNumbers = [
    ['000', 
     '0 0', 
     '0 0', 
     '0 0', 
     '000'],
    [' 1 ',
     '11 ',
     ' 1 ',
     ' 1 ',
     '111',],
    ['222',
     '  2',
     '222',
     '2  ',
     '222'],
    ['333',
     '  3',
     '333',
     '  3',
     '333',],
    ['4 4',
     '4 4',
     '444',
     '  4',
     '  4',],
    ['555',
     '5  ',
     '555',
     '  5',
     '555',],
    ['666',
     '6  ',
     '666',
     '6 6',
     '666',],
    ['777',
     '  7',
     '  7',
     '  7',
     '  7',],
    ['888',
     '8 8',
     '888',
     '8 8',
     '888',],
    ['999',
     '9 9',
     '999',
     '  9',
     '999',],
    [' ',
    ':',
    ' ',
    ':',
    ' ']
]

#### print the output line by line ####
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
    for x in range(len(myNumbers[0])): print(two[x],seporator[x], three[x], four[x] + ' ')
else:
    for x in range(len(myNumbers[0])): print(one[x], two[x],seporator[x], three[x], four[x] + ' ')
