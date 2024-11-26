board={1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12:' ', 13: ' ', 14: ' ', 15: ' ', 16: ' '}
print("Enter a letter.")
let=input()
def printboard():
    print(board[1],let, '|',board[2],let, '|',board[3],let, '|',board[4],let)
    print('-----------------------')
    print(board[5],let, '|',board[6],let, '|',board[7],let, '|',board[8],let)
    print('-----------------------')
    print(board[9],let, '|',board[10],let, '|',board[11],let, '|',board[12],let)
    print('-----------------------')
    print(board[13],let, '|',board[14],let, '|',board[15],let, '|',board[16],let)


def checkwin():
    if board[1]==board[2]==board[3]==board[4] and board[1]!=' ':
        return True
    if board[5]==board[6]==board[7]==board[8] and board[5]!=' ':
        return True
    if board[9]==board[10]==board[11]==board[12] and board[9]!=' ':
        return True
    if board[13]==board[14]==board[15]==board[16] and board[13]!=' ':
        return True
    if board[1]==board[6]==board[11] ==board[16] and board[1]!=' ':
        return True
    if board[4]==board[7]==board[10]==board[13] and board[4]!=' ':
        return True
    if board[1]==board[5]==board[9]==board[13] and board[1]!=' ':
        return True
    if board[2]==board[6]==board[10]==board[14] and board[2]!=' ':
        return True
    if board[3]==board[7]==board[11]==board[15] and board[3]!=' ':
        return True
    if board[4]==board[8]==board[12]==board[16] and board[4]!=' ':
        return True
    return False
print("Welcome to the Tic Tac Toe game!")
printboard()
print("Enter your name(X)")
name=input()
print("Enter your name(O)")
name=input()


moves=0
score=0
score2=0


import random    
player1='X'

while True:
    print("************************************************")
    print(player1,"Turn")
    if player1=='O':
        position=random.randint(1,16)
    else:
        position=int(input("Pick a spot(1-16): "))
        
    if board[position] == ' ':
        board[position]=player1
        moves=moves+1
        printboard()
        if checkwin():            
            print(player1,"has won the game!")
            break        
        if moves==9:
            print("The game is a tie!")
            break
        if player1=='X':
            player1='O'
        else:
            player1='X'
    else:
        print("Already taken")
            

printboard()

