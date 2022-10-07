# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Riley Hebert
#               Triston Maresh
#               Malcolm Ferguson
#               Marissa Bosher
# Section:      504
# Assignment:   Topic 7 program
# Date:         3 October, 2022
#


# note that as long as its in the outer brackets, you can
# use multiple lines for the stuff inside of the list
board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".",
             ".", ".", ".", "."],
         [".", ".", ".", ".", ".",
             ".", ".", ".", "."],
         [".", ".", ".", ".", ".",
             ".", ".", ".", "."],
         [".", ".", ".", ".", ".",
             ".", ".", ".", "."],
         [".", ".", ".", ".", ".",
             ".", ".", ".", "."],
         [".", ".", ".", ".", ".",
             ".", ".", ".", "."],
         [".", ".", ".", ".", ".",
             ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]

play = True
player = "Black"
while play == True: # this loop contains the entire game loop
    print("The board looks like this: ")
    for i in board: # this loop prints the board each turn
        print('\n', end=" ")
        for space in i:
            print(space, end=" ")

    print(f"\nIt is currently {player}'s turn")
    xInput = input("Please input an integer for the column: ")
    if (xInput == "stop"): # this checks if the input was 'stop'
        break
    else:
        xInput = int(xInput) # converts the xInput to an integer for use in accessing indexes later
        if not (xInput in range(9)):
            print("That value is not valid. Valid values are integers 0 to 8 inclusive.")
            continue # skips the rest of this iteration of the while loop

    yInput = input("Please input an integer for the row: ")
    if (yInput == "stop"): # this checks if the input was stop
        break
    else:
        yInput = int(yInput) # converts the yInput to an integer for use in accessing indexes later
        if (not (xInput in range(9) or not (yInput in range(9)))):
            print("That value is not valid, Valid values are integers 0 to 8 inclusive.")
            continue # skips the rest of this iteration of the while loop

    if (board[yInput][xInput] != "."): # checks if the space was NOT empty
        print("no no no that space is not EMPTEEEEEE, try again!")
        continue
    elif (board[yInput][xInput] == "."): # if the space is empty
        if (player == "Black"):
            board[yInput][xInput] = "O"
            player = "White"
        elif (player == "White"):
            board[yInput][xInput] = "o"
            player = "Black"
