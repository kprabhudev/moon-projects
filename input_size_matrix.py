row=list()
matrix=list()
def printRow(size, symbol):
    row = [symbol for i in range (size)]
    for item in row:
        print('',item,'|', end='')
    print()
    for i in range(size):
        print('----', end='')
       
print("Enter a number.")
size=int(input())
print("Enter a symbol.")
symbol=input()
def printMatrix(size, symbol):
    for i in range(size):
        printRow(size, symbol)
        print()

printMatrix(size, symbol)
