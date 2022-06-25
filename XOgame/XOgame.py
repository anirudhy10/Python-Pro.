# variables containg position of maze
xstate=[0,0,0,0,0,0,0,0,0]
zstate=[0,0,0,0,0,0,0,0,0]
turn =1

def sum(a,b,c):
    return a+b+c

# function printing game board
def printBoard(xstate,zstate):
    zero= 'X ' if xstate[0] else  ('O ' if zstate[0] else '0 ') # var for each position containing notation 
    one= 'X ' if xstate[1] else('O '  if zstate[1] else '1 ')
    two= 'X ' if xstate[2] else ('O ' if zstate[2] else '2 ')
    three= 'X ' if xstate[3] else ('O ' if zstate[3] else '3 ')
    four= 'X ' if xstate[4] else ('O ' if zstate[4] else '4 ')
    five= 'X ' if xstate[5] else ('O ' if zstate[5] else '5 ')
    six= 'X ' if xstate[6] else ('O ' if zstate[6] else '6 ')
    seven= 'X ' if xstate[7] else ('O ' if zstate[7] else '7 ')
    eight= 'X ' if xstate[8] else ('O ' if zstate[8] else '8 ')
    
    #maze print
    print(f"{zero}|{one}|{two}")
    print(f"--|--|--")
    print(f"{three}|{four}|{five}")
    print(f"--|--|--")
    print(f"{six}|{seven}|{eight}")


    #checking game winning conditions
def Wincheck(xstate,zstate):
    xwin=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwin:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("X Won the Match")
            return 1
        if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
            print("O Won the Match")
            return 0
    return -1

#main body of the game
print("Welcome to tic tac toe")
while(True):
    printBoard(xstate,zstate)
    if(turn==1):
        print("X's Chance")
        value=int(input("Enter position: "))
        xstate[value]=1
    else:
        print("O's Chance")
        value=int(input("Enter position: "))
        zstate[value]=1
    check=Wincheck(xstate,zstate)
    if(check!=-1):
        print("Match Over")
        break
    turn= 1-turn

