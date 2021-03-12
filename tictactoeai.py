import random
### function for computer to play specific moves
def computerAI(liste):
    # array for playable areas
    playable = []
    for i in range(3):
        for j in range(3):
            if(liste[i][j] == "-"):
                playable.append([i,j])

    ################################### put 3rd "O" if there are 2 ###################################
    ##### rows #####
    # row 0 #
    if liste[0][0] == "O" and liste[0][1] == "O" and liste[0][2] == "-":
        liste[0][2] = "O"
    elif liste[0][0] == "O" and liste[0][2] == "O" and liste[0][1] == "-":
        liste[0][1] = "O"
    elif liste[0][1] == "O" and liste[0][2] == "O" and liste[0][0] == "-":
        liste[0][0] = "O"

    # row 1 #
    elif liste[1][0] == "O" and liste[1][1] == "O" and liste[1][2] == "-":
        liste[1][2] = "O"
    elif liste[1][0] == "O" and liste[1][2] == "O" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "O" and liste[1][2] == "O" and liste[1][0] == "-":
        liste[1][0] = "O"

    # row 2 #
    elif liste[2][0] == "O" and liste[2][1] == "O" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[2][0] == "O" and liste[2][2] == "O" and liste[2][1] == "-":
        liste[2][1] = "O"
    elif liste[2][1] == "O" and liste[2][2] == "O" and liste[2][0] == "-":
        liste[2][0] = "O"

    ##### columns #####
    # column 0 #
    elif liste[0][0] == "O" and liste[1][0] == "O" and liste[2][0] == "-":
        liste[2][0] = "O"
    elif liste[0][0] == "O" and liste[2][0] == "O" and liste[1][0] == "-":
        liste[1][0] = "O"
    elif liste[1][0] == "O" and liste[2][0] == "O" and liste[0][0] == "-":
        liste[0][0] = "O"

    # column 1 #
    elif liste[0][1] == "O" and liste[1][1] == "O" and liste[2][1] == "-":
        liste[2][1] = "O"
    elif liste[0][1] == "O" and liste[2][1] == "O" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "O" and liste[2][1] == "O" and liste[0][1] == "-":
        liste[0][1] = "O"

    # column 2 #
    elif liste[0][2] == "O" and liste[1][2] == "O" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[0][2] == "O" and liste[2][2] == "O" and liste[1][2] == "-":
        liste[1][2] = "O"
    elif liste[1][2] == "O" and liste[2][2] == "O" and liste[0][2] == "-":
        liste[0][2] = "O"

    ##### diagonals #####
    # topleft to downright #
    elif liste[0][0] == "0" and liste[1][1] == "0" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[0][0] == "0" and liste[2][2] == "0" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "O" and liste[2][2] == "O" and liste[0][0] == "-":
        liste[0][0] = "O"

    # downleft to topright #
    elif liste[0][2] == "0" and liste[1][1] == "0" and liste[2][0] == "-":
        liste[2][0] = "O"
    elif liste[0][2] == "0" and liste[2][0] == "0" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "O" and liste[2][0] == "O" and liste[0][2] == "-":
        liste[0][2] = "O"

    ################################### put "O" if there are 2 "X"s ###################################
    ##### rows #####
    # row 0 #
    elif liste[0][0] == "X" and liste[0][1] == "X" and liste[0][2] == "-":
        liste[0][2] = "O"
    elif liste[0][0] == "X" and liste[0][2] == "X" and liste[0][1] == "-":
        liste[0][1] = "O"
    elif liste[0][1] == "X" and liste[0][2] == "X" and liste[0][0] == "-":
        liste[0][0] = "O"

    # row 1 #
    elif liste[1][0] == "X" and liste[1][1] == "X" and liste[1][2] == "-":
        liste[1][2] = "O"
    elif liste[1][0] == "X" and liste[1][2] == "X" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "X" and liste[1][2] == "X" and liste[1][0] == "-":
        liste[1][0] = "O"

    # row 2 #
    elif liste[2][0] == "X" and liste[2][1] == "X" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[2][0] == "X" and liste[2][2] == "X" and liste[2][1] == "-":
        liste[2][1] = "O"
    elif liste[2][1] == "X" and liste[2][2] == "X" and liste[2][0] == "-":
        liste[2][0] = "O"

    ##### columns #####
    # column 0 #
    elif liste[0][0] == "X" and liste[1][0] == "X" and liste[2][0] == "-":
        liste[2][0] = "O"
    elif liste[0][0] == "X" and liste[2][0] == "X" and liste[1][0] == "-":
        liste[1][0] = "O"
    elif liste[1][0] == "X" and liste[2][0] == "X" and liste[0][0] == "-":
        liste[0][0] = "O"

    # column 1 #
    elif liste[0][1] == "X" and liste[1][1] == "X" and liste[2][1] == "-":
        liste[2][1] = "O"
    elif liste[0][1] == "X" and liste[2][1] == "X" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "X" and liste[2][1] == "X" and liste[0][1] == "-":
        liste[0][1] = "O"

    # column 2 #
    elif liste[0][2] == "X" and liste[1][2] == "X" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[0][2] == "X" and liste[2][2] == "X" and liste[1][2] == "-":
        liste[1][2] = "O"
    elif liste[1][2] == "X" and liste[2][2] == "X" and liste[0][2] == "-":
        liste[0][2] = "O"

    ##### diagonals #####
    # topleft to downright #
    elif liste[0][0] == "X" and liste[1][1] == "X" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[0][0] == "X" and liste[2][2] == "X" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "X" and liste[2][2] == "X" and liste[0][0] == "-":
        liste[0][0] = "O"

    # downleft to topright #
    elif liste[0][2] == "X" and liste[1][1] == "X" and liste[2][0] == "-":
        liste[2][0] = "O"
    elif liste[0][2] == "X" and liste[2][0] == "X" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "X" and liste[2][0] == "X" and liste[0][2] == "-":
        liste[0][2] = "O"

    ##################################### put "O" if there are 1 ######################################
    ##### rows #####
    # row 0 #
    elif liste[0][0] == "O" or liste[0][1] == "O" and liste[0][2] == "-":
        liste[0][2] = "O"
    elif liste[0][0] == "O" or liste[0][2] == "O" and liste[0][1] == "-":
        liste[0][1] = "O"
    elif liste[0][1] == "O" or liste[0][2] == "O" and liste[0][0] == "-":
        liste[0][0] = "O"

    # row 1 #
    elif liste[1][0] == "O" or liste[1][1] == "O" and liste[1][2] == "-":
        liste[1][2] = "O"
    elif liste[1][0] == "O" or liste[1][2] == "O" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "O" or liste[1][2] == "O" and liste[1][0] == "-":
        liste[1][0] = "O"

    # row 2 #
    elif liste[2][0] == "O" or liste[2][1] == "O" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[2][0] == "O" or liste[2][2] == "O" and liste[2][1] == "-":
        liste[2][1] = "O"
    elif liste[2][1] == "O" or liste[2][2] == "O" and liste[2][0] == "-":
        liste[2][0] = "O"

    ##### columns #####
    # column 0 #
    elif liste[0][0] == "O" or liste[1][0] == "O" and liste[2][0] == "-":
        liste[2][0] = "O"
    elif liste[0][0] == "O" or liste[2][0] == "O" and liste[1][0] == "-":
        liste[1][0] = "O"
    elif liste[1][0] == "O" or liste[2][0] == "O" and liste[0][0] == "-":
        liste[0][0] = "O"

    # column 1 #
    elif liste[0][1] == "O" or liste[1][1] == "O" and liste[2][1] == "-":
        liste[2][1] = "O"
    elif liste[0][1] == "O" or liste[2][1] == "O" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "O" or liste[2][1] == "O" and liste[0][1] == "-":
        liste[0][1] = "O"

    # column 2 #
    elif liste[0][2] == "O" or liste[1][2] == "O" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[0][2] == "O" or liste[2][2] == "O" and liste[1][2] == "-":
        liste[1][2] = "O"
    elif liste[1][2] == "O" or liste[2][2] == "O" and liste[0][2] == "-":
        liste[0][2] = "O"

    ##### diagonals #####
    # topleft to downright #
    elif liste[0][0] == "0" or liste[1][1] == "0" and liste[2][2] == "-":
        liste[2][2] = "O"
    elif liste[0][0] == "0" or liste[2][2] == "0" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "O" or liste[2][2] == "O" and liste[0][0] == "-":
        liste[0][0] = "O"

    # downleft to topright #
    elif liste[0][2] == "0" or liste[1][1] == "0" and liste[2][0] == "-":
        liste[2][0] = "O"
    elif liste[0][2] == "0" or liste[2][0] == "0" and liste[1][1] == "-":
        liste[1][1] = "O"
    elif liste[1][1] == "O" or liste[2][0] == "O" and liste[0][2] == "-":
        liste[0][2] = "O"

    ################### play random playable area if there are no other options #######################
    else:
        cp = int(random.random()*(len(playable))) #sayı
        oPut = playable[cp]
        row = oPut[0]
        column = oPut[1] 
        liste[row][column] = "O"