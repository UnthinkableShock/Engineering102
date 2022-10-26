# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Riley Hebert
#               Triston Maresh
#               Malcolm Ferguson
#               Marissa Bosher
# Section:      504
# Assignment:   Topic 9 program
# Date:         26 October, 2022
#

def getpoints(myList):
    myPairs = myList.split(' ')
    for i in range(len(myPairs)): # loops through the big list
        myPairs[i] = myPairs[i].split(',') # splits the strings into their own list
        for n in range(len(myPairs[i])): #loop through the pairs and convert to ints
            myPairs[i][n] = int(myPairs[i][n])
    return myPairs

def cross(point1, point2):
    return (point1[0] * point2[1]) - (point1[1] * point2[0])
    

def shoelace(listOfPoints):
    result = 0
    for i in range(-1, len(listOfPoints) - 1): # takes each set of points, adds all the results of cross together
        result = result + cross(listOfPoints[i], listOfPoints[i+1]) / 2
    return result
    
def main():
    myString = input("Please enter the vertices: ")
    #myString = '2,3 4,5 27,43 2,7'
    print(f"The area of the polygon is {shoelace(getpoints(myString))}")

if __name__ == '__main__':
    main()