# NIM
# Alicia Wade
# CSCI 77800 Fall 2022

#set player 
player = 1

#set number of objetcs
stones = '12'
print("The number of stones is ", stones)

while True:
    #valid move
    print("Player ", player)
    while True:
        move = int(input ("How many stones do you want to take? (1, 2 or 3)"))
        if move in [1,2,3] and move < int(stones):
            break
        print("Not a valid move")
    #update the state
    stones = int(stones)-move

    #show the state
    print("The number of stones is  ", stones)
    
    #check the win status - win, lose
    if stones == 1:
        print("Player ", player, "wins!")
        break
    
    #switch the players
    if player == 1:
        player = 2
    else:
        player = 1
        
print("Game is over.")


