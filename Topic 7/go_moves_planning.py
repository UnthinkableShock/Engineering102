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
player = "player 1"
while play == True:
    print("The board looks like this: ")
    for i in board:
        print('\n', end=" ")
        for space in i:
            print(space, end=" ")

    print(f"\nIt is currently {player}'s turn")
    xInput = input("Please input an integer for the column: ")
    if (xInput == "stop"):  # this checks if the input was 'stop'
        play = False
        break
    else:
        xInput = int(xInput)

    yInput = input("Please input an integer for the row: ")
    if (yInput == "stop"):
        play = False
        break
    else:
        yInput = int(yInput)

    if (board[yInput][xInput] != "."):
        print("no no no that space is not EMPTEEEEEE, try again.")
    elif (board[yInput][xInput] == "."):
        if (player == "player 1"):
            board[yInput][xInput] = " O "
            player = "player 2"
        elif (player == "player 2"):
            board[yInput][xInput] = " o "
            player = "player 1"
