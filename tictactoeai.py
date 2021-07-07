import random
### function for computer to play specific moves


def readMoves(mapCode):
    with open("playableMoves.txt", "r") as file:
        liste = file.read().splitlines()
    moveList = []
    for i in liste:
        moveList.append(i.split("-"))

    returnList = []
    for j in moveList:
        if j[0] == mapCode:
            returnList.append(j)

    return returnList


def removeFromList(moveList):
    # Removes given move from list of moves.
    move = "-".join(moveList)

    with open("playableMoves.txt", "r+") as file:
        liste = file.read().splitlines()

    index = None
    found = 0
    for i in range(len(liste)):
        if liste[i] == move:
            index = i
            found += 1

    if found == 1:
        liste.pop(index)
        with open("playableMoves.txt", "r+") as file:
            file.truncate(0)
            for i in liste:
                file.writelines(i + "\n")


def computerAI(coor, symbol):
    """    # array for playable areas
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
        liste[row][column] = "O"""

    mapCodeList = []
    for i in range(3):
        for j in range(3):
            mapCodeList.append(coor[i][j])
    mapCode = "".join(mapCodeList)

    playableMovesList = readMoves(mapCode)
    print(playableMovesList)

    lastList = []
    for k in playableMovesList:
        if k[2] == symbol:
            lastList.append(k)

    move = random.choice(lastList)
    return move
