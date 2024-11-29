

matrix=[]

def printRow(size, symbol):
    row = [symbol for i in range (size)]
    for item in row:
        print('',item,'|', end='')
    print()
    for i in range(size):
        print('----', end='')
        
def buildMatrix(size, symbol):
    for i in range(size):
        matrix.append([symbol] * size)
    
    
def updateMatrix(row, col, symbol):
    matrix[1][1] = symbol
    
def printMatrix():
    matrixSize = len(matrix)
    for i in range(matrixSize):
        print(f"{i+1 : ^3}", end="|")
        for j in range(matrixSize):
            print('',matrix[i][j],'|', end='')
        print()
        
        
def winCheck():
    size = len(matrix)
    win = False
    for row in range(size):
        win = True
        for col in range(size):
            if matrix[row][col] == "_":
                win = False
                break
            if matrix[row][col] != matrix[row][0]:
                win = False;
                break
        if win == True:
            return True
        
    return win
    
def playGame():
    size = int(input("Etner the size"))
    buildMatrix(size, "_")
    printMatrix()
    player1="X"
    player2="O"
    moveCount=0
    playerList=[player1,player2]
    currentPlayer = playerList[0]
    
    while moveCount < size*size:
        print("Player-",(moveCount%2)+1, end=' ')
        position = int(input(", Etner your postition: "))
        if(position < 1 or position > (size*size)):
            print("Valid position range:1-", size*size, end = '. ')
            continue
        position = position - 1
        row = position // size
        col = position % size
        if matrix[row][col] != "_":
            print("Position already taken. ", end = '')
            continue
        currentPlayer = playerList[moveCount % 2]
        matrix[row][col] = currentPlayer
        if winCheck() == True:
            print ("Player-",(moveCount%2)+1," wins the game !")
            return
        printMatrix()
        moveCount += 1
        
    print ("Game Drawn :(")

playGame()   

