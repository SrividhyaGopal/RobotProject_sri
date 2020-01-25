from random import randrange, uniform


def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    for elem in board:
        for j in range(3):
            print ("|  ",elem[j],"  ",end="")
        print("|")
        print("|       |       |       |")
        print("+-------+-------+-------+")
        print("|       |       |       |")

def EnterMove(board):
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    pos = int(input("Please enter your position between 0 to less than 10 and cannot point to occupied"))
    for i in range(3) :
        for j in range(3):
            if pos == board[i][j]:
                board[i][j]='0'
                return 0
    #DisplayBoard(board)

def MakeListOfFreeFields(board):
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    lst =[]
    for i in range(3) :
        for j in range(3):
            if( board[i][j]!= '0' and board[i][j]!='X'):
                lst += [(i,j)]
    #print("free list is ",lst)
    return lst
def VictoryFor(board, sign):
    # the function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    signlst = []
    for i in range(3) :
        for j in range(3):
            if( board[i][j]== sign):
                signlst += [(i,j)]
    print(sign,signlst)
    for i in range (3):
        if((i,0) in signlst and (i,1) in signlst and (i,2) in signlst):
            #print("winner by row")
            return 1
    for i in range (3):
        if((0,i) in signlst and (1,i) in signlst and (2,i) in signlst):
            #print("winner by column")
            return 1
    if((1,1) in signlst ):
        counter =0
        for i in range(3):
            if((i,i) in signlst):
                counter += 1
        if(counter ==3):
           #print("winner by diagonal")
           return 1
        elif((2,0) in signlst and (0,2) in signlst):
           print("winner by diagonal other")
           return 1
def DrawMove(board):
    #the function draws the computer's move and updates the board
    # randrange gives you an integral value
    irand = randrange(0, 10)
    print(" computer choice is " , irand)
    for i in range(3) :
        for j in range(3):
            if irand == board[i][j]:
                board[i][j]='X'
                return 0
def MakeListOf0Fields(board):
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    lst0 =[]
    for i in range(3) :
        for j in range(3):
            if( board[i][j]== '0'):
                lst0 += [(i,j)]
    #print("0 list is ",lst0)
    return lst0    
def MakeListOfXFields(board):
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    lstX =[]
    for i in range(3) :
        for j in range(3):
            if( board[i][j]== 'X'):
                lstX += [(i,j)]
    #print("X list is ",lstX)
    return lstX   
board = [[1,2,3],[4,'X',6],[7,8,9]]
while True:
    DisplayBoard(board)
    check=0
    check = EnterMove(board)
    while(check!=0):
        print(" 1 ",check)
        DisplayBoard(board)
        print("please enter a proper input")
        check = EnterMove(board)
        DisplayBoard(board)
    freelst = MakeListOfFreeFields(board)
    if(len(freelst)==0):
        print("No one is the winner")
        break  
    if(len(freelst)<=3):
        list0 = MakeListOf0Fields(board)
        listX = MakeListOfXFields(board)
        if(len(list0) == len(listX)):
            returnVal = VictoryFor(board, 'X')
            if (returnVal == 1):
                print("Computer is the winner")
                break
            returnVal = VictoryFor(board, '0')
            if (returnVal == 1):
                print("You are the winner")
                break
    check=0
    check = DrawMove(board)
    while(check!=0):
        print(" 2 ",check)
        DisplayBoard(board)
        print("enter a proper input")
        check = DrawMove(board)
    
    
    
    
    
    





