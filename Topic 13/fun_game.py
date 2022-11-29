

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

# import turtle package
import turtle
import numpy as np

def draw_circle(myTurtle, color='red', radius=20):
    """
    draws a circle for the indicated turtle
    """
    myTurtle.fillcolor(color)
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()
    return 0

def setup_turtle(destination=[], color="red", xpos=-350, ypos=225, radius = 20, width=1):
    """
    sets up the turtle at a particular spot, with a particular color
    """
    myTurtle = turtle.Turtle()
    myTurtle.color(color)
    myTurtle.speed(0)
    myTurtle.width(1)
    myTurtle.hideturtle() # hides the turtle
    myTurtle.penup()
    myTurtle.goto(xpos, ypos)
    myDict = {
        "turtle":myTurtle,
        "side":color,
        "moving":True,
        "startPos":[xpos, ypos],
        "destination":destination,
        "phase":0,
        "angle":-np.pi/2,
        "rad":50,
        "color":color,
        "radius":radius,
        "destiny 2":"a bad game",
        "Riley":"confused",

    }
    return myDict

def setup(width=700, height=700, color='gray'):
    canvas = turtle.Screen()     
    canvas.setup(width, height)
    canvas.bgcolor(color)
    canvas.tracer(0) # tracer controls wether or not it shows the animation
    return canvas

def new_turtle(myTurtles, destination, color = 'red'):
    myTurtles.append(setup_turtle(destination, color))
    return 0

def rules():
    print("Welcome to the game of Connect Four!")
    print("The rules are simple:")
    print("1. In order to win, you need to get 4 in a row diagonally, horizontally, or vertically.")
    print("2. If a column is full, you cannot place a piece in that column")
    print("3. Pieces stack on top of other pieces previously placed in the same column")
    print("4. At any time, you can quit the game by inputting 'exit'")
    print("5. At any time, you can get the rules again by inputting 'help'\n")
    print("As a sidenote, it would be wise to have half the screen be turtle, \nand the other half be the command line or IDE you are using, to make it easier to play\n")
    return 0

def drawBoard(canvas, boardXRange, boardYRange):
    """
    draws the whole board using lines
    """
    canvas.tracer(0)
    xStep = (boardXRange[1]-boardXRange[0])
    yStep = (boardYRange[1]-boardYRange[0])
    maxX = max(boardXRange) + (boardXRange[1]-boardXRange[0])
    minX = min(boardXRange)
    maxY = max(boardYRange) + (boardYRange[1]-boardYRange[0])
    minY = min(boardYRange)
    myBoard = turtle.Turtle()
    myBoard.hideturtle()
    for i in range(0, len(boardXRange)+1):
        xpos = boardXRange[0]-20 + i*xStep
        myBoard.penup()
        myBoard.goto(xpos, minY-40)
        myBoard.pendown()
        myBoard.goto(xpos, maxY-40)

    for i in range(0, len(boardYRange)+1):
        ypos = boardYRange[0]-40 + (i)*yStep
        myBoard.penup()
        myBoard.goto(minX-20, ypos)
        myBoard.pendown()
        myBoard.goto(maxX-20, ypos)
    
    myBoard.penup()
    canvas.tracer(0)

def main():
    canvas = setup(800, 900)
    myTurtles = []
    board = [] # first index will be rows, second index will be columns
    boardXRange = np.linspace(-250, 230, 7)
    boardYRange = np.linspace(-315, 130, 6)
    pieceCount = [0, 0, 0, 0, 0, 0, 0]

    drawBoard(canvas, boardXRange, boardYRange) # draws the board for connect 4

    #for i in range(6):
    #    for n in range(7):
    #        new_turtle(myTurtles, targetColumn, boardXRange, boardYRange)
    
    for i in range(6):
        myList = []
        for i in range(7):
            myList.append('x')
        board.append(myList)
    rules() # prints out a set of the rules
    game = True
    player = "blue"
    while game: # the game is contained in this loop
        print("Valid columns are integers 1 through 7, inclusive")
        getInput = True
        while getInput: # loop to get valid input
            try:
                targetColumn = input("It is currently {player}'s turn.\nPlease choose a column to insert a piece: ")
                if targetColumn == "exit":
                    game = False
                    break
                if targetColumn == "help":
                    rules()
                    continue
                targetColumn = int(targetColumn) - 1 # tries to convert to int
                if targetColumn >= 0 and targetColumn <= 6: # if the value is in the right range
                    if pieceCount[targetColumn] < 6: # if the column isnt full
                        new_turtle(myTurtles, [boardXRange[targetColumn], boardYRange[pieceCount[targetColumn]]], player)
                        pieceCount[targetColumn] += 1

                        # changes which players' turn it is
                        if (player == "blue"):
                            player = "red"
                        elif (player == "red"):
                            player = "blue"
                        break
                    else:
                        print("Sorry, that column is already full, pick a different one!")
                else:
                    print("That is not a valid input! Your input needs to be between 1 and 7 inclusive!")
            except:
                print(f"That is not a valid input! Your input needs to be an integer!")
        if game == False: # stops it from drawing the turtles if the game is over
            break
        for sillyTurtle in myTurtles:
            while sillyTurtle["phase"] != 4:
                # clear sillyTurtle work
                sillyTurtle["turtle"].clear()
                # call function to draw ball
                draw_circle(sillyTurtle["turtle"], sillyTurtle["color"], sillyTurtle["radius"])
                rad = sillyTurtle["rad"]
                angle = sillyTurtle["angle"]
                xtar = sillyTurtle["destination"][0]+rad
                ytar = sillyTurtle["startPos"][1]+rad
                if sillyTurtle["phase"] == 0: # phase 0 is just coming onto the screen
                    if abs(sillyTurtle["turtle"].xcor() - sillyTurtle["destination"][0] - rad) <= 1:
                        sillyTurtle["phase"] += 1
                        continue
                    sillyTurtle["turtle"].setheading(0)
                    sillyTurtle["turtle"].forward(1)
                if sillyTurtle["phase"] == 1: # phase 1 is where the fun part is: LOOP DE LOOP WHOOOOOP!!!
                    if abs(angle - np.pi) <= 0.01:
                        sillyTurtle["phase"] += 1
                        continue
                    sillyTurtle["turtle"].goto(xtar + rad*np.cos(angle), ytar + rad*np.sin(angle))
                    sillyTurtle["angle"] += 0.01
                    
                        
                if sillyTurtle["phase"] == 2:
                    #sillyTurtle["sillyTurtle"].goto(xtar + rad*np.cos(np.pi), ytar + rad*np.sin(np.pi))
                    sillyTurtle["turtle"].goto(sillyTurtle["destination"][0], ytar)
                    sillyTurtle["phase"] += 1
                if sillyTurtle["phase"] == 3:
                    if abs(sillyTurtle["turtle"].xcor() - sillyTurtle["destination"][0]) <= 0.1 and abs(sillyTurtle["turtle"].ycor() - sillyTurtle["destination"][1]) <= 0.1:
                        sillyTurtle["phase"] += 1
                        break
                    else:
                        sillyTurtle["turtle"].setheading(-90)
                        sillyTurtle["turtle"].forward(1)

                # update the screen
                canvas.update()

if __name__ == "__main__":
    main()
