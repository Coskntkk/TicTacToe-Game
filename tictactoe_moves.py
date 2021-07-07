from itertools import permutations


def listAllTictactoeMoves():
    permutates = []
    coorNames = ["         ", "X        ", "XO       ", "XOX      ", "XOXO     ", "XOXOX    ", "XOXOXO   ", "XOXOXOX  ", "XOXOXOXO ", "O        ", "OX       ", "OXO      ", "OXOX     ", "OXOXO    ", "OXOXOX   ", "OXOXOXO  ", "OXOXOXOX "]
    for i in coorNames:
        permutates.append(set(["".join(p) for p in permutations(i)]))
    finalList = set.union(permutates[0], permutates[1], permutates[2], permutates[3], permutates[4], permutates[5], permutates[6], permutates[7], permutates[8], permutates[9], permutates[10], permutates[11], permutates[12], permutates[13], permutates[14], permutates[15])
    finalList = list(finalList)

    removeList = []
    for i in finalList:

        if i[0] == i[1] == i[2] == "X" or i[0] == i[1] == i[2] == "O":
            removeList.append(i)
        elif i[3] == i[4] == i[5] == "X" or i[3] == i[4] == i[5] == "O":
            removeList.append(i)
        elif i[6] == i[7] == i[8] == "X" or i[6] == i[7] == i[8] == "O":
            removeList.append(i)

        elif i[0] == i[3] == i[6] == "X" or i[0] == i[3] == i[6] == "O":
            removeList.append(i)
        elif i[1] == i[4] == i[7] == "X" or i[1] == i[4] == i[7] == "O":
            removeList.append(i)
        elif i[2] == i[5] == i[8] == "X" or i[2] == i[5] == i[8] == "O":
            removeList.append(i)

        elif i[0] == i[4] == i[8] == "X" or i[0] == i[4] == i[8] == "O":
            removeList.append(i)
        elif i[2] == i[4] == i[6] == "X" or i[2] == i[4] == i[6] == "O":
            removeList.append(i)

    for i in removeList:
        if i in finalList:
            finalList.remove(i)

    tileList = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
    sideList = ["X", "O"]

    allMovesList = []
    for i in finalList:
        for j in range(len(tileList)):
            for k in sideList:
                if i[j] == " ":
                    allMovesList.append(f"{i}-{tileList[j]}-{k}")

    with open("all_tictactoe_moves.txt", "a") as file:
        file.truncate(0)
        for i in allMovesList:
            file.writelines(i+"\n")

    with open("playableMoves.txt", "a") as file:
        file.truncate(0)
        for i in allMovesList:
            file.writelines(i+"\n")

listAllTictactoeMoves()