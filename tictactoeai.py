from random import choice
### function for computer to play specific moves


def computerAI(liste, side):
    opposite = ""
    empty = "-"
    if side == "O":
        opposite = "X"
    elif side == "X":
        opposite = "O"

    ################################### put 3rd side if there are 2 ###################################
    ##### rows #####
    # row 0 #
    if liste[0][0] == side and liste[0][1] == side and liste[0][2] == empty:
        liste[0][2] = side
    elif liste[0][0] == side and liste[0][2] == side and liste[0][1] == empty:
        liste[0][1] = side
    elif liste[0][1] == side and liste[0][2] == side and liste[0][0] == empty:
        liste[0][0] = side

    # row 1 #
    elif liste[1][0] == side and liste[1][1] == side and liste[1][2] == empty:
        liste[1][2] = side
    elif liste[1][0] == side and liste[1][2] == side and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == side and liste[1][2] == side and liste[1][0] == empty:
        liste[1][0] = side

    # row 2 #
    elif liste[2][0] == side and liste[2][1] == side and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[2][0] == side and liste[2][2] == side and liste[2][1] == empty:
        liste[2][1] = side
    elif liste[2][1] == side and liste[2][2] == side and liste[2][0] == empty:
        liste[2][0] = side

    ##### columns #####
    # column 0 #
    elif liste[0][0] == side and liste[1][0] == side and liste[2][0] == empty:
        liste[2][0] = side
    elif liste[0][0] == side and liste[2][0] == side and liste[1][0] == empty:
        liste[1][0] = side
    elif liste[1][0] == side and liste[2][0] == side and liste[0][0] == empty:
        liste[0][0] = side

    # column 1 #
    elif liste[0][1] == side and liste[1][1] == side and liste[2][1] == empty:
        liste[2][1] = side
    elif liste[0][1] == side and liste[2][1] == side and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == side and liste[2][1] == side and liste[0][1] == empty:
        liste[0][1] = side

    # column 2 #
    elif liste[0][2] == side and liste[1][2] == side and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[0][2] == side and liste[2][2] == side and liste[1][2] == empty:
        liste[1][2] = side
    elif liste[1][2] == side and liste[2][2] == side and liste[0][2] == empty:
        liste[0][2] = side

    ##### diagonals #####
    # topleft to downright #
    elif liste[0][0] == side and liste[1][1] == side and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[0][0] == side and liste[2][2] == side and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == side and liste[2][2] == side and liste[0][0] == empty:
        liste[0][0] = side

    # downleft to topright #
    elif liste[0][2] == side and liste[1][1] == side and liste[2][0] == empty:
        liste[2][0] = side
    elif liste[0][2] == side and liste[2][0] == side and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == side and liste[2][0] == side and liste[0][2] == empty:
        liste[0][2] = side

    ################################### put side if there are 2 opposites ###################################
    ##### rows #####
    # row 0 #
    elif liste[0][0] == opposite and liste[0][1] == opposite and liste[0][2] == empty:
        liste[0][2] = side
    elif liste[0][0] == opposite and liste[0][2] == opposite and liste[0][1] == empty:
        liste[0][1] = side
    elif liste[0][1] == opposite and liste[0][2] == opposite and liste[0][0] == empty:
        liste[0][0] = side

    # row 1 #
    elif liste[1][0] == opposite and liste[1][1] == opposite and liste[1][2] == empty:
        liste[1][2] = side
    elif liste[1][0] == opposite and liste[1][2] == opposite and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == opposite and liste[1][2] == opposite and liste[1][0] == empty:
        liste[1][0] = side

    # row 2 #
    elif liste[2][0] == opposite and liste[2][1] == opposite and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[2][0] == opposite and liste[2][2] == opposite and liste[2][1] == empty:
        liste[2][1] = side
    elif liste[2][1] == opposite and liste[2][2] == opposite and liste[2][0] == empty:
        liste[2][0] = side

    ##### columns #####
    # column 0 #
    elif liste[0][0] == opposite and liste[1][0] == opposite and liste[2][0] == empty:
        liste[2][0] = side
    elif liste[0][0] == opposite and liste[2][0] == opposite and liste[1][0] == empty:
        liste[1][0] = side
    elif liste[1][0] == opposite and liste[2][0] == opposite and liste[0][0] == empty:
        liste[0][0] = side

    # column 1 #
    elif liste[0][1] == opposite and liste[1][1] == opposite and liste[2][1] == empty:
        liste[2][1] = side
    elif liste[0][1] == opposite and liste[2][1] == opposite and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == opposite and liste[2][1] == opposite and liste[0][1] == empty:
        liste[0][1] = side

    # column 2 #
    elif liste[0][2] == opposite and liste[1][2] == opposite and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[0][2] == opposite and liste[2][2] == opposite and liste[1][2] == empty:
        liste[1][2] = side
    elif liste[1][2] == opposite and liste[2][2] == opposite and liste[0][2] == empty:
        liste[0][2] = side

    ##### diagonals #####
    # topleft to downright #
    elif liste[0][0] == opposite and liste[1][1] == opposite and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[0][0] == opposite and liste[2][2] == opposite and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == opposite and liste[2][2] == opposite and liste[0][0] == empty:
        liste[0][0] = side

    # downleft to topright #
    elif liste[0][2] == opposite and liste[1][1] == opposite and liste[2][0] == empty:
        liste[2][0] = side
    elif liste[0][2] == opposite and liste[2][0] == opposite and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == opposite and liste[2][0] == opposite and liste[0][2] == empty:
        liste[0][2] = side

    ##################################### put side if there are 1 ######################################
    ##### rows #####
    # row 0 #
    elif liste[0][0] == side or liste[0][1] == side and liste[0][2] == empty:
        liste[0][2] = side
    elif liste[0][0] == side or liste[0][2] == side and liste[0][1] == empty:
        liste[0][1] = side
    elif liste[0][1] == side or liste[0][2] == side and liste[0][0] == empty:
        liste[0][0] = side

    # row 1 #
    elif liste[1][0] == side or liste[1][1] == side and liste[1][2] == empty:
        liste[1][2] = side
    elif liste[1][0] == side or liste[1][2] == side and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == side or liste[1][2] == side and liste[1][0] == empty:
        liste[1][0] = side

    # row 2 #
    elif liste[2][0] == side or liste[2][1] == side and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[2][0] == side or liste[2][2] == side and liste[2][1] == empty:
        liste[2][1] = side
    elif liste[2][1] == side or liste[2][2] == side and liste[2][0] == empty:
        liste[2][0] = side

    ##### columns #####
    # column 0 #
    elif liste[0][0] == side or liste[1][0] == side and liste[2][0] == empty:
        liste[2][0] = side
    elif liste[0][0] == side or liste[2][0] == side and liste[1][0] == empty:
        liste[1][0] = side
    elif liste[1][0] == side or liste[2][0] == side and liste[0][0] == empty:
        liste[0][0] = side

    # column 1 #
    elif liste[0][1] == side or liste[1][1] == side and liste[2][1] == empty:
        liste[2][1] = side
    elif liste[0][1] == side or liste[2][1] == side and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == side or liste[2][1] == side and liste[0][1] == empty:
        liste[0][1] = side

    # column 2 #
    elif liste[0][2] == side or liste[1][2] == side and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[0][2] == side or liste[2][2] == side and liste[1][2] == empty:
        liste[1][2] = side
    elif liste[1][2] == side or liste[2][2] == side and liste[0][2] == empty:
        liste[0][2] = side

    ##### diagonals #####
    # topleft to downright #
    elif liste[0][0] == side or liste[1][1] == side and liste[2][2] == empty:
        liste[2][2] = side
    elif liste[0][0] == side or liste[2][2] == side and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == side or liste[2][2] == side and liste[0][0] == empty:
        liste[0][0] = side

    # downleft to topright #
    elif liste[0][2] == side or liste[1][1] == side and liste[2][0] == empty:
        liste[2][0] = side
    elif liste[0][2] == side or liste[2][0] == side and liste[1][1] == empty:
        liste[1][1] = side
    elif liste[1][1] == side or liste[2][0] == side and liste[0][2] == empty:
        liste[0][2] = side

    ################### play random playable area if there are no other options #######################
    else:
        playable = []
        for i in range(3):
            for j in range(3):
                if liste[i][j] == empty:
                    playable.append([i, j])
        move = choice(playable)
        liste[move[0]][move[1]] = side
