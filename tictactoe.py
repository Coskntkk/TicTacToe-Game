import random
# this is a simple tic-tac-toe game
# ----------------- GLOBAL VARIABLES ----------------- 

# liste that is the map of tic-tac-toe
liste = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]

# empty areas on map
playable = []

win_check = False

# print map
def maps(liste):
    map = """
      | 0 | 1 | 2 | 
    --+---+---+---+
    0 | {} | {} | {} 
    --+---+---+---+
    1 | {} | {} | {} 
    --+---+---+---+
    2 | {} | {} | {} 
    """.format(liste[0][0],liste[0][1],liste[0][2],liste[1][0],liste[1][1],liste[1][2],liste[2][0],liste[2][1],liste[2][2])
    return map


# player movement 
def playerMove(liste):
    print("Player 1's turn.")
    row = int(input("Row: "))
    column = int(input("Column: "))
    if(liste[row][column] == "-"):
        liste[row][column] = "X"
    else:
        print("Player can't move here.")
        print("Try again.")
        playerMove(liste)
    print(maps(liste))

# player2 movement
def player2Move(liste):
    print("Player 2's turn.")
    row = int(input("Row: "))
    column = int(input("Column: "))
    if(liste[row][column] == "-"):
        liste[row][column] = "O"
    else:
        print("Player can't move here.")
        print("Try again.")
        player2Move(liste)
    print(maps(liste))

# computer movement
def computerMove(liste,playable):
    playable = []
    for i in range(3):
        for j in range(3):
            if(liste[i][j] == "-"):
                playable.append([i,j])
    cp = int(random.random()*(len(playable))) #sayı
    oPut = playable[cp]
    row = oPut[0]
    column = oPut[1] 
    liste[row][column] = "O"

    print("Computer moved")
    print(maps(liste))


# function to check if there is any win situation
def winCheck(liste):
    # check row 
    for row in range(3):
        if(liste[row][0] == liste[row][1] and liste[row][0] == liste[row][2] and liste[row][0] != "-"):
            return True

    # check column 
    for column in range(3):
        if(liste[0][column] == liste[1][column] and liste[0][column] == liste[2][column] and liste[0][column] != "-"):
            return True

    # check diagonally
    if(liste[0][0] == liste[1][1] and liste[0][0] == liste[2][2] and liste[1][1] != "-"):
        return True
    if(liste[0][2] == liste[1][1] and liste[0][2] == liste[2][0] and liste[1][1] != "-"):
        return True

    # there is no win..
    else:
        return False

# player vs computer mod
def gamePvC():
    print("""Player is "X".""")
    print(maps(liste))
    print("-------------------------------")
    while(winCheck(liste) == False):
        playerMove(liste)
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Player won.")
            break
        computerMove(liste,playable)
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Computer won.")
            break

# player vs player mod
def gamePvP():
    print("""Player 1 is "X".""")
    print("""Player 2 is "O".""")    
    print(maps(liste))
    while(winCheck(liste) == False):
        playerMove(liste)
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Player 1 won.")
            break
        player2Move(liste)
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Player 2 won.")
            break

# main menu function
def main():
    print("Welcome to Tic-Tac-Toe Game! ")
    print("Choose one:")
    print("""
1 - Read Tic-Tac-Toe Rules
2 - Play Tic-Tac-Toe against computer.
3 - Play Tic-Tac-Toe against player.
""") 
    choice = int(input(">>>"))
    if(choice == 1):
        print("this is a game.")
        choice2 = input("wanna play? (y/n)")
        if(choice2 == "y" or choice2 == "Y"):
            main()
        else:
            game_exit()
    elif(choice == 2): 
        gamePvC()
    elif(choice == 3):
        gamePvP()
    play_again = input("Do you want to play again? (Y/N): ")
    if(play_again == "Y" or play_again == "y"):
        main()
    elif(play_again == "N" or play_again == "n"):
        game_exit()

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
        # draw option is not recognized yet.
# 07.03.21
        # pvp option added


# CREDITS: CAGLA & COSKUN 