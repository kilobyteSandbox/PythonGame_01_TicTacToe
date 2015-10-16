# =====================================
# This is a text version of Tic Tac Toe
# =====================================


# Possible player moves on the board
gameBoard = {'a1': ' ', 'b1': ' ', 'c1': ' ',
             'a2': ' ', 'b2': ' ', 'c2': ' ',
             'a3': ' ', 'b3': ' ', 'c3': ' ',}


def intro():
    print("============")
    print("Tic Tac Toe!")
    print("============")
    print(" ")


# Prints player options
def printOptions():
    print("a1 | b1 | c1")
    print("-- + -- + --")
    print("a2 | b2 | c2")
    print("-- + -- + --")
    print("a3 | b3 | c3")
    print(" ")


# Prints the board
def printBoard(board):
    # Ascii used for drawing the board
    vert = "|"
    horiz = "-"
    cross = "+"
    space = " "
    # Silly formatting variables for the board
    moveLineFormat = space + vert + space
    gridLineFormat = horiz + space + cross + space
    gridLineBlock = gridLineFormat + gridLineFormat + horiz
    # Prints the board with game in progress
    print(board['a1'] + moveLineFormat + board['b1'] + moveLineFormat + board['c1'])
    print(gridLineBlock)
    print(board['a2'] + moveLineFormat + board['b2'] + moveLineFormat + board['c2'])
    print(gridLineBlock)
    print(board['a3'] + moveLineFormat + board['b3'] + moveLineFormat + board['c3'])
    print(" ")


# Check to see if player has won.  I would do this programmatically if it was 4x4, but for now, delicious
# spaghetti code.
def checkWin(mark):
    # Hobo shorthand for board values
    a1 = gameBoard['a1']
    a2 = gameBoard['a2']
    a3 = gameBoard['a3']
    b1 = gameBoard['b1']
    b2 = gameBoard['b2']
    b3 = gameBoard['b3']
    c1 = gameBoard['c1']
    c2 = gameBoard['c2']
    c3 = gameBoard['c3']
    # Hobo check horizontal sets of 3
    if a1 == mark and b1 == mark and c1 == mark:
        return True
    if a2 == mark and b2 == mark and c2 == mark:
        return True
    if a3 == mark and b3 == mark and c3 == mark:
        return True
    # Hobo check vertical sets of 3
    if a1 == mark and a2 == mark and a3 == mark:
        return True
    if b1 == mark and b2 == mark and b3 == mark:
        return True
    if c1 == mark and c2 == mark and c3 == mark:
        return True
    # Hobo check diagonals
    if a1 == mark and b2 == mark and c3 == mark:
        return True
    if c1 == mark and b2 == mark and a3 == mark:
        return True
    else:
        return False


def gameOver(player, moves):
    if player == "X":
        print("X has won in " + str(moves) + " turns!")
    else:
        print("O has won in " + str(moves) + " turns!")


# Plays a game of Tic Tac Toe
def playGame():
    # Start with player X
    player = "X"
    print("Let's begin!")
    print(" ")
    # After 9 moves, the game is over
    i = 0
    while i < 9:
        # Print board and start turn
        printBoard(gameBoard)
        print("It is " + player + "'s turn.  Pick a space from a1 to c3.")
        print(" ")
        move = input()
        print(" ")
        print(" ")
        # Check if input is valid
        if move not in gameBoard.keys():
            print("Sorry, that is not a valid move.  Please pick a space from a1 to c3.")
            printOptions()
        # Check if move is valid
        elif gameBoard[move] != ' ':
            print("Sorry, that space has alrady been taken.  Please pick another space from a1 to c3.")
            print(" ")
            printBoard(gameBoard)
        # Update player move, increment turn counter
        else:
            gameBoard[move] = player
            i += 1
            # Check to see if a move won
            if checkWin(player) == True:
                gameOver(player, i)
                print(" ")
                break
            # See if all moves are used
            if i == 9:
                print("The game ended in a draw.")
                print(" ")
                break
            # If game continues, set from X to O or O to X
            if player == "X":
                player = "O"
            else:
                player = "X"




# Program start
intro()
printOptions()
playGame()
printBoard(gameBoard)
print("Game over!")