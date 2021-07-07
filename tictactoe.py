import tictactoeai
import time

# this is a simple tic-tac-toe game
# ----------------- GLOBAL VARIABLES ----------------- 

# liste that is the map of tic-tac-toe
liste = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

# empty areas on map
playable = []

win_check = False


# print map
def maps():
    global liste

    board = """
      | 0 | 1 | 2 | 
    --+---+---+---+
    0 | {} | {} | {} 
    --+---+---+---+
    1 | {} | {} | {} 
    --+---+---+---+
    2 | {} | {} | {} 
    """.format(liste[0][0], liste[0][1], liste[0][2], liste[1][0], liste[1][1], liste[1][2], liste[2][0], liste[2][1], liste[2][2])
    print(board)


# player movement 
def playerMove():
    global liste
    print(liste)

    print("Player 1's turn.")
    row = int(input("Row: "))
    column = int(input("Column: "))
    if liste[row][column] == " ":
        liste[row][column] = "X"
    else:
        print("Player can't move here.")
        print("Try again.")
        playerMove()
    maps()


# player2 movement
def player2Move():
    global liste

    print("Player 2's turn.")
    row = int(input("Row: "))
    column = int(input("Column: "))
    if liste[row][column] == " ":
        liste[row][column] = "O"
    else:
        print("Player can't move here.")
        print("Try again.")
        player2Move()
    maps()


# computer movement
def computerMove(side):
    global liste
    move = tictactoeai.computerAI(liste, side)
    liste[int(move[1][0])][int(move[1][1])] = move[2]

    print("Computer moved")
    maps()

    return move


# function to check if there is any win situation
def winCheck():
    global liste

    # check row 
    for row in range(3):
        if liste[row][0] == liste[row][1] and liste[row][0] == liste[row][2] and liste[row][0] != " ":
            return True

    # check column 
    for column in range(3):
        if liste[0][column] == liste[1][column] and liste[0][column] == liste[2][column] and liste[0][column] != " ":
            return True

    # check diagonally
    if liste[0][0] == liste[1][1] and liste[0][0] == liste[2][2] and liste[1][1] != " ":
        return True
    if liste[0][2] == liste[1][1] and liste[0][2] == liste[2][0] and liste[1][1] != " ":
        return True

    # there is no win..
    else:
        return False


# function for waiting
def waiting():
    print("Computer moving")
    print("...")
    time.sleep(0.75)
    print("..")
    time.sleep(0.75)
    print(".")
    time.sleep(0.75)


# player vs computer mod
def gamePvC():
    global liste

    print("""Player is "X".""")
    maps()
    print("-------------------------------")
    pvcCount = 9
    while True:
        playerMove()
        pvcCount -= 1
        print("-------------------------------")
        if winCheck():
            print("Player won.")
            break
        if pvcCount == 0:
            print("Draw. Nobody won, nobody lost.")
            break
        waiting()
        computerMove("O")  # ##############################################
        pvcCount -= 1
        print("-------------------------------")
        if winCheck():
            print("Computer won.")
            break
        if pvcCount == 0:
            print("Draw. Nobody won, nobody lost.")
            break


# computer vs computer mod
def gameCvC():
    global liste

    print("""Computer 1 is "X".""")
    print("""Computer 2 is "O".""")
    maps()
    print("-------------------------------")
    pvcCount = 9

    playedMoves = []

    while True:
        playedMoves.append(computerMove("X"))
        pvcCount -= 1
        print("-------------------------------")
        if winCheck():
            print("Player won.")
            print(playedMoves)
            tictactoeai.removeFromList(playedMoves[-2])
            break
        if pvcCount == 0:
            print("Draw. Nobody won, nobody lost.")
            break
        #waiting()

        playedMoves.append(computerMove("O"))  # ##############################################
        pvcCount -= 1
        print("-------------------------------")
        if winCheck():
            print("Computer won.")
            print(playedMoves)
            tictactoeai.removeFromList(playedMoves[-2])
            break
        if pvcCount == 0:
            print("Draw. Nobody won, nobody lost.")
            break
        #waiting()



# player vs player mod
def gamePvP():
    global liste

    print("""Player 1 is "X".""")
    print("""Player 2 is "O".""")
    maps()
    print("-------------------------------")
    pvpCount = 9
    while not winCheck():
        playerMove()
        pvpCount -= 1
        print("-------------------------------")
        if winCheck():
            print("Player 1 won.")
            break
        if pvpCount == 0:
            print("Draw. Nobody won, nobody lost.")
            break
        player2Move()
        pvpCount -= 1
        print("-------------------------------")
        if winCheck():
            print("Player 2 won.")
            break
        if pvpCount == 0:
            print("Draw. Nobody won, nobody lost.")
            break


# main menu function
def main():
    global liste

    """print("Welcome to Tic-Tac-Toe Game! ")
    print("Choose one:")
    print(
1 - Read Tic-Tac-Toe Rules
2 - Play Tic-Tac-Toe against computer.
3 - Play Tic-Tac-Toe against player.
4 - Play Tic-Tac-Toe computer vs computer.
)
    choice = int(input(">>>"))
    if choice == 1:
        print("this is a game.")
        choice2 = input("wanna play? (y/n)")
        if choice2 == "y" or choice2 == "Y":
            main()
        else:
            game_exit()
    elif choice == 2:
        liste = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        gamePvC()
    elif choice == 3:
        liste = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        gamePvP()
    elif choice == 4:
        gameCvC()
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again == "Y" or play_again == "y":
        main()
    elif play_again == "N" or play_again == "n":
        game_exit()"""
    for i in range(50):
        liste = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        gameCvC()


def game_exit():
    print("Bye...")


# 1 - Read Tic-Tac-Toe Rules
# 2 - Play Tic-Tac-Toe
main()

# UPDATES -->
# 06.03.21
# simple win mechanic is implemented.
# menu added
# need to be improved:
# game explanation is.. a bit short.
# computer is silly af
# 07.03.21
# pvp option added
# draw option is recognized.

# CREDITS: CAGLA & COSKUN
