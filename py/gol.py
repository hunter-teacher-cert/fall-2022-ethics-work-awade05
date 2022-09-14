# GOL
# Alicia Wade
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: GOL from Java, Codeacademy, stackoverflow on how to create the board 

import random
#create a new board 
def createNewBoard(rows, cols):
  return [['X']*cols for X in range(rows)]

# set cell (r,c) to val
def setCell(board, r, c, val):
    board[r][c] = val

#print board
def printBoard(board):
    rows = len(board)
    cols = len(board[0])
    
    for r in range(0, rows):
        for c in range(0,cols):
            print(board[r][c] + " ", end =' ')
        print()

#count neighbors
def countNeighbors(board, r, c):
    rows = len(board)
    cols = len(board[0])
    neighborCount = 0
    
    for i in range (0,rows):
      for j in range( 0, cols):
    #excludes the square itself and checks the area around
         if( \
            not(i == r and j == c) \
            and (i <= r+1 and i >= r-1) \
            and (j <= c+1 and j >= c-1) ):
              if(board[i][j] == "X"):
                neighborCount = neighborCount + 1       
    return neighborCount  
    
#next generation cell state
def getNextGenCell(board, r, c):
    gen = board[r][c]
    count = countNeighbors(board,r,c)
    nextGen = "0"
    
    
    #cell is alive
    if (gen == 'X'):
          #lonely and overcrowded
      if (count < 2 or count >3):
        nextGen = 'X'
     #dead cell
      else:
        nextGen = "0"
    else:
    #dead but has three alive neighbors
        if (count == 3):  
          nextGen = 'X'
        else:
            nextGen = '0'
    return nextGen

#generate and return new board
def generateNextBoard(board):
    rows = len(board)
    cols = len(board)
    
    newGameBoard = createNewBoard(rows, cols)
    
    for r in range(0,rows):
        for c in range(0,rows):
            gen = getNextGenCell(board,r,c)
        newGameBoard[r][c] = gen
        
    return newGameBoard

board = \
  [ \
    ['0','0','X','0','X','0'], \
    ['0','X','X','0','0','X'], \
    ['0','0','X','X','X','X'], \
    ['0','0','0','0','X','0'], \
    ['X','0','0','0','X','X'], \
    ['0','0','0','0','X','X'],\
  ]
printBoard(board)
for i in range(20):
  print()
  board = generateNextBoard(board)
  printBoard(board)

   
