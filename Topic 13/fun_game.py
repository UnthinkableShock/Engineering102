# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Riley Hebert
#               Triston Maresh
#               Malcolm Ferguson
#               Marissa Bosher
# Section:      504
# Assignment:   Topic 13 fun game py file
# Date:         29 November, 2022
#

# import turtle package
import turtle
import numpy as np

##### setup #####

class myTurtle:
    def __init__(self, myTurtles, destination, color):
        self.xpos = -350
        self.ypos = 225
        self.data = {
        "turtle":turtle.Turtle(),
        }
        self.data["turtle"].color(color)
        self.data["turtle"].speed(0)
        self.data["turtle"].width(1)
        self.data["turtle"].hideturtle() # hides the turtle
        self.data["turtle"].penup() # makes it so that the turtle doesn't leave behind a trail
        self.data["turtle"].goto(self.xpos, self.ypos) # go to the starting point, off screen
        self.side = color
        self.startPos = [self.xpos, self.ypos]
        self.destination = destination
        self.phase = 0
        self.angle = -np.pi/2
        self.rad = 50
        self.color = color
        self.radius = 20
        myTurtles.append(self)
        

def setup():
    canvas = turtle.Screen()     
    canvas.setup(700, 800)
    canvas.bgcolor('gray')
    canvas.tracer(0) # tracer controls wether or not it shows the animation
    board = [['x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x']] # first index will be rows, second index will be columns
    myStuff = {
        "myTurtles":[],
        "canvas":canvas,
        "board":board, 
        "boardXRange":np.linspace(-250, 230, 7), 
        "boardYRange":np.linspace(-315, 130, 6), 
        "pieceCount":[0, 0, 0, 0, 0, 0, 0],
    }
    drawBoard(myStuff)
    return myStuff

def drawBoard(myStuff):
    canvas = myStuff["canvas"]
    boardXRange = myStuff["boardXRange"]
    boardYRange = myStuff["boardYRange"]
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
    return 0

##############

def rules():
    """
    Prints the rules into the console
    """
    print("Welcome to the game of Connect Four! This version is meant for 2 players.")
    print("The rules are simple:")
    print("1. In order to win, you need to get 4 of your color pieces in a row diagonally, horizontally, or vertically.")
    print("2. If a column is full, you cannot place a piece in that column")
    print("3. Pieces stack on top of other pieces previously placed in the same column\n")
    print("Options:")
    print("'exit' : inputting 'exit' will exit the game")
    print("'help' : inputting 'help' will bring up the rules again")
    print("'log' : inputting 'log' will print out all recorded events, like moves made, into the console")
    print("\nAs a sidenote, being able to see both the cmd line and the turtle window\nat the same time will make it easier to play\n")
    return 0

##############

def drawCircle(myTurtle, color='red', radius=20):
    """
    draws a circle using the indicated turtle
    """
    myTurtle.data["turtle"].fillcolor(color)
    myTurtle.data["turtle"].begin_fill()
    myTurtle.data["turtle"].circle(radius)
    myTurtle.data["turtle"].end_fill()
    return 0

def phase0(sillyTurtle):
    """
    phase0 makes the turtle move from off screen to on screen
    """
    if sillyTurtle.phase == 0: # phase 0 is just coming onto the screen
        if sillyTurtle.data["turtle"].xcor() - sillyTurtle.destination[0] - sillyTurtle.rad >= 0:
            sillyTurtle.phase += 1
            return True
        else:
            sillyTurtle.data["turtle"].setheading(0)
            sillyTurtle.data["turtle"].forward(5)
            return False
    else:
        return False

def phase1(sillyTurtle, angle, xtar, ytar):
    """
    Makes the turtle perform a Loop de loop. Need I say more?
    """
    if sillyTurtle.phase == 1: # phase 1 is where the fun part is: LOOP DE LOOP WHOOOOOP!!!
        if angle - np.pi > 0.01:
            sillyTurtle.phase += 1
            return True
        else:
            sillyTurtle.data["turtle"].goto(xtar + sillyTurtle.rad*np.cos(angle), ytar + sillyTurtle.rad*np.sin(angle))
            sillyTurtle.angle += 0.05
            return False
    else:
        return False

def phase2(sillyTurtle, ytar):
    """
    places the turtle in a spot where it lines up with its destination
    """
    if sillyTurtle.phase == 2:
        sillyTurtle.data["turtle"].goto(sillyTurtle.destination[0], ytar)
        sillyTurtle.phase += 1
    else:
        return False

def phase3(sillyTurtle):
    """
    makes the turtle go down until it reaches it's destination
    """
    if sillyTurtle.phase == 3:
        if (sillyTurtle.data["turtle"].xcor() - sillyTurtle.destination[0] < 0.1) and (sillyTurtle.data["turtle"].ycor() - sillyTurtle.destination[1]) < 0.1:
            sillyTurtle.phase += 1
            return True
        else:
            sillyTurtle.data["turtle"].setheading(-90)
            sillyTurtle.data["turtle"].forward(5)
            return False
    else:
        return False

def animateTurtle(sillyTurtle, canvas):
    """
    Will move the pieces as needed
    """
    while sillyTurtle.phase != 4: # each "phase" corresponds to different movements
        # clear sillyTurtle work
        sillyTurtle.data["turtle"].clear()
        # call function to draw ball
        drawCircle(sillyTurtle, sillyTurtle.color, sillyTurtle.radius)
        rad = sillyTurtle.rad
        angle = sillyTurtle.angle
        xtar = sillyTurtle.destination[0]+rad
        ytar = sillyTurtle.startPos[1]+rad
        
        if phase0(sillyTurtle): # moves turtle, but the if x then continue makes it so that the other phases dont get accidentally triggered
            continue
        elif phase1(sillyTurtle, angle, xtar, ytar): # LOOP DE LOOP WHOOP!
            continue
        elif phase2(sillyTurtle, ytar): # fixes its position
            continue
        elif phase3(sillyTurtle): # checks for it to reach the end destination
            break

        # update the screen
        canvas.update()
    return 0

##############

def check(myStuff):
    """
    checks the board for 4 in a row
    """
    board = myStuff["board"]
    players = ["blue", "red"]
    for myPlayer in players:
        aPlayer, won = checkStraight(board, myPlayer)
        aPlayer2, won2 = checkDiagonal(board, myPlayer)
        if (won):
            log_action(myStuff, f"{aPlayer} won! Congratulations!")
            return aPlayer, won
        elif (won2):
            log_action(myStuff, f"{aPlayer} won! Congratulations!")
            return aPlayer2, won2
        else:
            return ['', False]

def checkStraight(board, myPlayer):
    for row in range(0, len(board)-3): # checks for vertical 4-in-a-row
            for column in range(0, len(board[0])):
                if (myPlayer[0] == board[row][column] == board[row+1][column] == board[row+2][column] == board[row+3][column]):
                    return myPlayer, True
                
    for column in range(0, len(board[0])-3): # checks for horizontal 4-in-a-row
        for row in range(0, len(board)):
            if (myPlayer[0] == board[row][column] == board[row][column+1] == board[row][column+2] == board[row][column+3]):
                return myPlayer, True
    return ['', False]

def checkDiagonal(board, myPlayer):
    for row in range(0, len(board)-3): # checks for diagonals 4-in-a-row 
            for column in range(0, len(board[0])-3):
                if (myPlayer[0] == board[row][column] == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3]):
                    return myPlayer, True
        
    for row in range(0, len(board)-3):
        for column in range(6, 2, -1): # checks for diagonal 4-in-a-row
            if (myPlayer[0] == board[row][column] == board[row+1][column-1] == board[row+2][column-2] == board[row+3][column-3]):
                print(f"{myPlayer} won!")
                return myPlayer, True
    return ['', False]

##############

def getInput(myStuff):
    player = myStuff["currentPlayer"]
    boardXRange = myStuff["boardXRange"]
    boardYRange = myStuff["boardYRange"]
    pieceCount = myStuff["pieceCount"]
    try: 
        ##### WE WANT YOU TO NOTE: the reason we don't have this big thing in smaller pieces is because this is just so much less painful
        targetColumn = input(f"\nIt is currently {player}'s turn.\nPlease choose a column to insert a piece: ")
        log_action(myStuff, f"User input: {targetColumn}")
        if targetColumn.lower() == "exit":
            log_action(myStuff, "Game was exited manually")
            return False
        if targetColumn.lower() == "help":
            log_action(myStuff, "Rules were printed in terminal")
            rules()
            return True
        if targetColumn.lower() == 'log':
            log_action(myStuff, "log was printed in terminal")
            log_print()
            return False
        targetColumn = int(targetColumn) - 1 # tries to convert to int
        if targetColumn >= 0 and targetColumn <= 6: # if the value is in the right range
            if pieceCount[targetColumn] < 6: # if the column isnt full
                myTurtle(myStuff["myTurtles"], [boardXRange[targetColumn], boardYRange[pieceCount[targetColumn]]], player)
                myStuff["board"][5 - pieceCount[targetColumn]][targetColumn] = player[0]
                myStuff["pieceCount"][targetColumn] += 1 # need to refer to the original dictionary if I want to change it
                # records the moves taken to display at the end
                log_action(myStuff, f"{player} put a piece in the {targetColumn+1} column at row {pieceCount[targetColumn]}\n")
                # changes which players' turn it is
                if (myStuff["currentPlayer"] == "blue"):
                    myStuff["currentPlayer"] = "red"
                elif (myStuff["currentPlayer"] == "red"):
                    myStuff["currentPlayer"] = "blue"
                return False
            else:
                log_action(myStuff, "Input Error - column was full")
                print("Sorry, that column is already full, pick a different one!")
                return True
        else:
            log_action(myStuff, "Input Error - input was not in range")
            print("That is not a valid input! Your input needs to be between 1 and 7 inclusive!")
            return True
    except:
        log_action(myStuff, "Input Error - input could not be converted to an integer")
        print(f"That is not a valid input! Your input needs to be an integer!")
        return True

##############

def log_action(myStuff, action):
    try:
        myLog = open('game_log.txt', 'a')
        myLog.write(f'{myStuff["counter"]} : {action}\n')
        myLog.close()
        myStuff["counter"] += 1
        return True
    except:
        myLog.close()
        return False

def log_print():
    """
    Prints the entirety of the current round's log
    """
    try:
        myLog = open('game_log.txt', 'r')
        print("##########################################")
        print("Current round's log:")
        for i in myLog.readlines():
            print(i.strip())
        myLog.close()
        return True
    except:
        myLog.close()
        return False

def main():
    """
    The entire game is run within this function
    """
    
    rules()
    myStuff = setup()
    myStuff["currentPlayer"] = "blue"
    myStuff["counter"] = 0
    game = True
    myMoves = open('game_log.txt', 'w')
    myMoves.write(f'{myStuff["counter"]} : Program was run\n')
    myStuff["counter"] += 1
    myMoves.close()

    while game: # the main loop of the game is contained in this while loop
        print("Valid columns are integers 1 through 7, inclusive")
        needInput = True
        while needInput: # while I need input, keep trying to get it
            needInput = getInput(myStuff)
        if game == False: # stops it from drawing the turtles if the game is already over
            break
        for sillyTurtle in myStuff["myTurtles"]: # loops through all the pieces
            animateTurtle(sillyTurtle, myStuff["canvas"]) # this function moves the turtles as needed
        winner, won = check(myStuff) # unpacking the stuff that the check() function returned
        if won: # if one of the players won
            print(f"\n{winner} has won this round of connect 4!\n")
            print("Would you like to play again?")
            print("Options:")
            print("'yes' - inputting 'yes' will start another round")
            print("'log' - inputting 'log' will print all the recorded events this round")
            print("input anything else to exit the game\n")
            playAgain = input("What do you choose?: ")
            log_action(myStuff, f"User input: {playAgain}")
            if (playAgain.lower() == 'yes'):
                log_action(myStuff, "The player decided to play again! YIPPEE!")
                myStuff["canvas"].clearscreen()
            elif (playAgain.lower() == 'log'):
                log_action(myStuff, "log was printed into terminal")
                log_print()
            else:
                log_action(myStuff, "The player decided not to play again, Oh well")
                print("Goodbye! Thank you for playing!")
                game = False

    return 0          

if __name__ == "__main__":
    main()