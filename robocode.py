#Robotic project
import random

def ShowBoard():
    print(board[0],"|",board[1],"|",board[2])
    print("---------")
    print(board[3],"|",board[4],"|",board[5])
    print("---------")
    print(board[6],"|",board[7],"|",board[8])

def GamewonCondition(char,spot1,spot2,spot3):
    if board[spot1]==char and board[spot2]==char and board[spot3]==char:
        return True
    else:
        return False

def Winner(char):
    if(GamewonCondition(char,0,1,2)):
        return True
    if(GamewonCondition(char,3,4,5)):
        return True
    if(GamewonCondition(char,6,7,8)):
        return True
    if(GamewonCondition(char,0,3,6)):
        return True
    if(GamewonCondition(char,1,4,7)):
        return True
    if(GamewonCondition(char,2,5,8)):
        return True
    if(GamewonCondition(char,0,4,8)):
        return True
    if(GamewonCondition(char,2,4,6)):
        return True
    return False

def GameDrawn(list):
    if(len(list) == 0):
        return True
    else:
        return False

def winningPosition(char,spot1,spot2):
    if board[spot1]==char and board[spot2]==char :
        return True
    else:
        return False

def WinningPlacement(char,list):
    if(winningPosition(char,0,1) and (2 in list)):
        return 2
        
    elif (winningPosition(char,1,2) and (0 in list)):
        return 0
        
    elif (winningPosition(char,0,2) and (1 in list)):
        return 1
    
    elif (winningPosition(char,3,4) and (5 in list)):
        return 5
     
    elif (winningPosition(char,4,5) and (3 in list)):
        return 3
       
    elif (winningPosition(char,3,5) and (4 in list)):
        return 4
    
    elif (winningPosition(char,6,7) and (8 in list)):
        return 8
    
    elif(winningPosition(char,7,8) and (6 in list)):
        return 6
        
    elif(winningPosition(char,6,8) and (7 in list)):
        return 7
      
    elif(winningPosition(char,0,3) and (6 in list)):
        return 6
        
    elif(winningPosition(char,3,6) and (0 in list)):
        return 0
    
    elif(winningPosition(char,0,6) and (3 in list)):
        return 3
    
    elif(winningPosition(char,1,4) and (7 in list)):
        return 7 
    
    elif(winningPosition(char,4,7) and (1 in list)):
        return 1
               
    elif(winningPosition(char,1,7) and (4 in list)):
        return 4
      
    elif(winningPosition(char,2,5) and (8 in list)):
        return 8
        
    elif(winningPosition(char,5,8) and (2 in list)):
        return 2
        
    elif(winningPosition(char,2,8) and (5 in list)):
        return 5
        
    elif(winningPosition(char,0,4) and (8 in list)):
        return 8
        
    elif(winningPosition(char,4,8) and (0 in list)):
        return 0
        
    elif(winningPosition(char,0,8) and (4 in list)):
        return 4
    
    elif(winningPosition(char,2,4) and (6 in list)):
        return 6
        
    elif(winningPosition(char,4,6) and (2 in list)):
        return 2
        
    elif(winningPosition(char,2,6) and (4 in list)):
        return 4

    #sdgdfhdfhd
    return 99


def RoboToWinPlacement(char,list):
    if(winningPosition(char,0,1) and (2 in list)):
        return 2
        
    elif (winningPosition(char,1,2) and (0 in list)):
        return 0
        
    elif (winningPosition(char,0,2) and (1 in list)):
        return 1
    
    elif (winningPosition(char,3,4) and (5 in list)):
        return 5
     
    elif (winningPosition(char,4,5) and (3 in list)):
        return 3
       
    elif (winningPosition(char,3,5) and (4 in list)):
        return 4
    
    elif (winningPosition(char,6,7) and (8 in list)):
        return 8
    
    elif(winningPosition(char,7,8) and (6 in list)):
        return 6
        
    elif(winningPosition(char,6,8) and (7 in list)):
        return 7
      
    elif(winningPosition(char,0,3) and (6 in list)):
        return 6
        
    elif(winningPosition(char,3,6) and (0 in list)):
        return 0
    
    elif(winningPosition(char,0,6) and (3 in list)):
        return 3
    
    elif(winningPosition(char,1,4) and (7 in list)):
        return 7 
    
    elif(winningPosition(char,4,7) and (1 in list)):
        return 1
               
    elif(winningPosition(char,1,7) and (4 in list)):
        return 4
      
    elif(winningPosition(char,2,5) and (8 in list)):
        return 8
        
    elif(winningPosition(char,5,8) and (2 in list)):
        return 2
        
    elif(winningPosition(char,2,8) and (5 in list)):
        return 5
        
    elif(winningPosition(char,0,4) and (8 in list)):
        return 8
        
    elif(winningPosition(char,4,8) and (0 in list)):
        return 0
        
    elif(winningPosition(char,0,8) and (4 in list)):
        return 4
    
    elif(winningPosition(char,2,4) and (6 in list)):
        return 6
        
    elif(winningPosition(char,4,6) and (2 in list)):
        return 2
        
    elif(winningPosition(char,2,6) and (4 in list)) :

        return 4
    else :
        return 99
    

board = [0,1,2,
         3,4,5,
         6,7,8]

vacantPlaces =  [0,1,2,
                 3,4,5,
                 6,7,8]

#user move tracker
userMoves=0

print("Robo plays using O and you plays form X")
ShowBoard()

while(True):
    print("\n")
    inputVal=int(input("Select the squer to place your X"))
    
    #check is the selected squre is a squre selected previously
    while(True):
        if(board[inputVal] == 'X' or board[inputVal] == 'O'):
            print("It's already selected.Select a another one ")
            inputVal=int(input("Select the squer to place your X"))
        else:
           board[inputVal] = 'X'
           userMoves=userMoves+1
           vacantPlaces.remove(inputVal)
           break

    #checking is the user won
    if(Winner('X')):
        print("You won")
        ShowBoard()
        break

    #check for the draw
    if(GameDrawn(vacantPlaces)):
        print("Game drawn")
        ShowBoard()
        break

    #check chance of Robo to win
    nextPlace=RoboToWinPlacement('O',vacantPlaces)
        
    if(nextPlace != 99):
        board[nextPlace]='O'
        vacantPlaces.remove(nextPlace)
        print("Robo chosed ", nextPlace)
        ShowBoard()

    else:
        nextPlace=WinningPlacement('X',vacantPlaces)#to block the user win

        if(nextPlace not in vacantPlaces and nextPlace != 99):
            nextPlace=random.choice(vacantPlaces)
        
        if(nextPlace != 99):
             board[nextPlace]='O'
             vacantPlaces.remove(nextPlace)
             print("Robo chosed ", nextPlace)
             ShowBoard()
        else:#if no one going to win Robo chose random place

            if(4 in vacantPlaces):
                nextPlace=4
                
            elif(8 in vacantPlaces):
                nextPlace=8
               
            elif(2 in vacantPlaces):
                nextPlace=2
                
            elif( 6 in vacantPlaces):
                nextPlace=6
               
            else:
                nextPlace=random.choice(vacantPlaces)

            board[nextPlace]='O'
            vacantPlaces.remove(nextPlace)
            print("Robo chosed ", nextPlace)
            ShowBoard()
        
    
    #checking is the ROBO won
    if(Winner('O')):
        print("Robo won")
        ShowBoard()
        break
    #check for the draw after ROBO move
    if(GameDrawn(vacantPlaces)):
        print("Game drawn")
        ShowBoard()
        break
