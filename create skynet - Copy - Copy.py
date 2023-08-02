import random
import sys
sys.setrecursionlimit(1000000000) 
from tkinter import *

#delcairing fonts
global large
large = ("arial", 55)
global medium
medium = ("arial",20)

#the Reaset button
def reinitialise():
    global root
    root.destroy()
    initialise()

def initialise():
    #declare spaces, turnCount and Corner global
    global turnCount
    turnCount = 1
    global spaces
    spaces = [0,0,0,0,0,0,0,0,0]
    global Corner
    global CVHFM
    #deciding who goes first via random
    CVHFM = random.choice([1,2])
    print("CVHFM =", CVHFM)
    #choosing starting move if comp go first
    if CVHFM == 1:
        Corner = random.choice([1,4])
        if Corner == 1:
            spaces = [2,0,0,0,0,0,0,0,0]
        if Corner == 2:
            spaces = [0,0,2,0,0,0,0,0,0]
        if Corner == 3:
            spaces = [0,0,0,0,0,0,0,0,2]
        if Corner == 4:
            spaces = [0,0,0,0,0,0,2,0,0]
    #declare game_over global and present values
    global game_over
    game_over = False
    #declare global buttons (holder for Tk button variables)
    global buttons
    buttons = []
    #declare global labels  (holder for Tk label variables)
    global labels
    labels = []
    #call start function to start running the program
    start()

def start(): #prepares root window
    #declare global called 'root'
    global root
    #build tkinter window
    root = Tk()
    root.wm_title('Tik Tac MOIK')
    root.minsize(width=1200, height=100) #try adjusting these
    Menubutton = Button(root, font = large, text='Restart', command = lambda: reinitialise())
    Menubutton.place(x=650,y=100)
    #building grid (horizonal and vertical lines) using loop (use a 'for' loop?)
    #loop to make variable r go 0, 2, 4
    for r in range(0,6,2):
        Label(root, font=large, text='|').grid(row=r, column=1)
        Label(root, font=large, text='|').grid(row=r, column=3)
    #end of loop
    #loop to make c go 0,1,2,3,4
    for c in range(0,5,1):
        Label(root, font=large, text='-').grid(row=1,column=c)
        Label(root, font=large, text='-').grid(row=3,column=c)
    #end of loop
    #call update_board function
    update_board()

#checks if the game is still going or over
def detect_win():
    return False
def take_moves(n):
    print("You triggered button ",n)
def decode_symbol(a):
    return ""

#define function 'available_spaces'
def available_spaces():
    #create an empty list called 'available_spaces'
    available_spaces = []
    #for each item in spaces
    for x in range(0,len(spaces)):
        #if the contents of the item is 0
        if spaces[x] == 0:
            #append the index of that item to the list 'available_spaces'
            available_spaces.append(x)
    #return the final list
    return available_spaces


def update_board(): #function to check if anyone has won and update the board
    #check if anyone has won
    #if detect win returns false, no winner, otherwise winner's name is returned
    if detect_win() != False: #if someone has won
        winner = detect_win() #get name of winner
        win_text = "Winner is: " + detect_win() #output name of winner
        Label(root,font=large, text=win_text).grid(row=5, column=0, columnspan=5)
    elif not (0 in spaces): #if nobody has one AND there are no blank spaces...
        #....it must be a draw
        Label(root, font=large, text='Draw!').grid(row=5, column=0, columnspan=5) #output 'draw'
    #clear out TK buttons for refresh
    for button in buttons:
        button.grid_forget()
    #clear out TK labels for refresh
    for label in labels:
        label.grid_forget()
    #create and position buttons and labels using loops
    x = 0 #x position
    y = 0 #y position
    n = 0 #index of button/label
    for space in spaces:
        if space == 0: #space not used yet, display button
            button = Button(root,text="  ", font=large, command=lambda n=n: take_moves(n))
            button.grid(row=y, column=x)
            buttons.append(button)
        else: #space has been used, so we should display value
            label = Label(root, font=large, text=decode_symbol(space)) #convert 1/2 into X/O
            label.grid(row=y, column=x)
            labels.append(label)
        x = x + 2 #move across 2
        if x>4: #if end of row
            x = 0 #...move to start
            y = y + 2 #...of next row
        n = n + 1 #increment button/label index
    root.mainloop() #wait for GUI action

def decode_symbol(code):#change code to symbol i.e. 0/1/2 => space/X/O
    sym = ["[]","X","O"]
    return sym[code]

def take_moves (usermove): #facilitates move
        #player move
        if usermove in available_spaces(): #if space requested by GUI is available (which it should be!)
                spaces[usermove] = 1 #save user move
        else:
                print("Error in function text_move: impossible move requested.")
                sys.exit(0)
        if detect_win()==False: #if nobody has won yet, let the computer take a move
                if len(available_spaces())>0: #computer move
                        Skynetview() #prints spaces left
                        #global rando
                        Skynet()
                                #def rando():
                                #print("les go rando")
                                #move = random.choice(available_spaces())
                                #spaces[move] = 2
                                #print("Spaces at end:",spaces)
                                #rando()
        else:
            game_over = True #no spaces available, must be the end of the game
        update_board() #refresh board

def doubleTcheck():
    print("Looking for the double threat...")
    pw = 0
    available_spaces_1 = available_spaces()
    if spaces[4] == spaces[8] == 2:
        if 0 in available_spaces_1:
            pw = pw + 1
    if spaces[0] == spaces[4] == 2:
        if 8 in available_spaces_1:
            pw = pw + 1
    if spaces[5] == spaces[8] == 2:
        if 2 in available_spaces_1:
            pw = pw + 1
    if spaces[7] == spaces[8] == 2:
        if 6 in available_spaces_1:
            pw = pw + 1
    if spaces[4] == spaces[7] == 2:
        if 1 in available_spaces_1:
            pw = pw + 1
    if spaces[6] == spaces[8] == 2:
        if 7 in available_spaces_1:
            pw = pw + 1
    if spaces[1] == spaces[7] == 2:
        if 4 in available_spaces_1:
            pw = pw + 1
    if spaces[2] == spaces[8] == 2:
        if 5 in available_spaces_1:
            pw = pw + 1
    if spaces[2] == spaces[5] == 2:
        if 8 in available_spaces_1:
            pw = pw + 1
    if spaces[6] == spaces[7] == 2:
        if 8 in available_spaces_1:
            pw = pw + 1
    if spaces[0] == spaces[6] == 2:
        if 3 in available_spaces_1:
            pw = pw + 1
    if spaces[6] == spaces[3] == 2:
        if 0 in available_spaces_1:
            pw = pw + 1
    if spaces[0] == spaces[3] == 2:
        if 6 in available_spaces_1:
            pw = pw + 1
    if spaces[6] == spaces[4] == 2:
        if 2 in available_spaces_1:
            pw = pw + 1
    if spaces[6] == spaces[2] == 2:
        if 4 in available_spaces_1:
            pw = pw + 1
    if spaces[4] == spaces[2] == 2:
        if 6 in available_spaces_1:
            pw = pw + 1
    if spaces[3] == spaces[4] == 2:
        if 5 in available_spaces_1:
            pw = pw + 1
    if spaces[3] == spaces[5] == 2:
        if 4 in available_spaces_1:
            pw = pw + 1
    if spaces[4] == spaces[5] == 2:
        if 2 in available_spaces_1:
            pw = pw + 1
    if spaces[0] == spaces[1] == 2:
        if 2 in available_spaces_1:
            pw = pw + 1
    if spaces[0] == spaces[2] == 2:
        if 1 in available_spaces_1:
            pw = pw + 1
    if spaces[1] == spaces[2] == 2:
        if 0 in available_spaces_1:
            pw = pw + 1
    if spaces[1] == spaces[4] == 2:
        if 7 in available_spaces_1:
            pw = pw + 1
    print("possible wins:",pw)        
    return pw

def doubleT():
    global double_threat_space
    print("double threat check initalised")
    double_threat_space = -1
    for space in available_spaces():
        spaces[space] = 2
        pw = doubleTcheck()
        pw = int(pw)
        if pw >= 2:
            print("found double threat in position",space)
            double_threat_space = space
        spaces[space] = 0
    if double_threat_space >= 0:
        print("double threat found")
        spaces[double_threat_space] = 2
    else:
        print("double threat not found")
        def prefernceTime():
            print("Checking the list")
            global turnCount
            global Corner
            global spaces
            if turnCount == 1:
                if CVHFM == 2:
                    RC = False
                    while RC == False:
                        Corner = random.choice([1,4])
                        if Corner == 1:
                            if spaces[0] == 0:
                                spaces = [2,0,0,0,0,0,0,0,0]
                                RC = True
                        if Corner == 2:
                            if spaces[2] == 0:
                                spaces = [0,0,2,0,0,0,0,0,0]
                                RC = True
                        if Corner == 3:
                            if spaces[8] == 0:
                                spaces = [0,0,0,0,0,0,0,0,2]
                                RC = True
                        if Corner == 4:
                            if spaces[6] == 0:
                                spaces = [0,0,0,0,0,0,2,0,0]
                                RC = True
            if turnCount == 2:
                if Corner == 1:
                    if spaces[8] == 0:
                        spaces[8] = 2
                    else:
                        choose = random.choice([1,2])
                        if choose == 1:
                            spaces[2] = 2
                        if choose == 2:
                            spaces[6] = 2
                if Corner == 2:
                    if spaces[6] ==0:
                        spaces[6] = 2
                    else:
                        choose = random.choice([1,2])
                        if choose == 1:
                            spaces[0] = 2
                        if choose == 2:
                            spaces[8] = 2
                if Corner == 3:
                    if spaces[0] == 0:
                        spaces[0] = 2
                    else:
                        choose = random.choice([1,2])
                        if choose == 1:
                            spaces[2] = 2
                        if choose == 2:
                            spaces[6] = 2
                if Corner == 4:
                    if spaces[2] == 0:
                        spaces[2] = 2
                    else:
                        choose = random.choice([1,2])
                        if choose == 1:
                            spaces[0] = 2
                        if choose == 2:
                            spaces[8] = 2
            else:
                def prefL2():
                    global turnCount
                    if turnCount == 3:
                        if spaces[0] == 0:
                            spaces[0] = 2
                        if spaces[2] == 0:
                            spaces[2] = 2
                        if spaces[6] == 0:
                            spaces[6] = 2
                        if spaces[8] == 0:
                            spaces[8] = 2
                    else:
                        rando()
                prefL2()
        def rando():
            print("les go rando")
            move = random.choice(available_spaces())
            spaces[move] = 2
            print("Spaces at end:",spaces)
        prefernceTime()
    return double_threat_space

def Skynetview():
    global turnCount
    turnCount = turnCount + 1
    print("Turn Count:", turnCount)
    #print(spaces)
    print(available_spaces())
def Skynet():
    Sspaces = [0 if x != 2 else 2 for x in spaces]
    #print(Sspaces)
    print("Spaces at start:",spaces)
    available_spaces_1 = available_spaces()
    move_taken = False
    print("Looking for the win...")
    if spaces[4] == spaces[8] == 2 and move_taken==False:
        if 0 in available_spaces_1:
            spaces[0] = 2
            move_taken = True
    if spaces[0] == spaces[8] == 2 and move_taken==False:
        if 4 in available_spaces_1:
            spaces[4] = 2
            move_taken = True
    if spaces[0] == spaces[4] == 2 and move_taken==False:
        if 8 in available_spaces_1:
            spaces[8] = 2
            move_taken = True
    if spaces[5] == spaces[8] == 2 and move_taken==False:
        if 2 in available_spaces_1:
            spaces[2] = 2
            move_taken = True
    if spaces[7] == spaces[8] == 2 and move_taken==False:
        if 6 in available_spaces_1:
            spaces[6] = 2
            move_taken = True
    if spaces[4] == spaces[7] == 2 and move_taken==False:
        if 1 in available_spaces_1:
            spaces[1] = 2
            move_taken = True
    if spaces[6] == spaces[8] == 2 and move_taken==False:
        if 7 in available_spaces_1:
            spaces[7] = 2
            move_taken = True
    if spaces[1] == spaces[7] == 2 and move_taken==False:
        if 4 in available_spaces_1:
            spaces[4] = 2
            move_taken = True
    if spaces[2] == spaces[8] == 2 and move_taken==False:
        if 5 in available_spaces_1:
            spaces[5] = 2
            move_taken = True
    if spaces[2] == spaces[5] == 2 and move_taken==False:
        if 8 in available_spaces_1:
            spaces[8] = 2
            move_taken = True
    if spaces[6] == spaces[7] == 2 and move_taken==False:
        if 8 in available_spaces_1:
            spaces[8] = 2
            move_taken = True
    if spaces[0] == spaces[6] == 2 and move_taken==False:
        if 3 in available_spaces_1:
            spaces[3] = 2
            move_taken = True
    if spaces[6] == spaces[3] == 2 and move_taken==False:
        if 0 in available_spaces_1:
            spaces[0] = 2
            move_taken = True
    if spaces[0] == spaces[3] == 2 and move_taken==False:
        if 6 in available_spaces_1:
            spaces[6] = 2
            move_taken = True
    if spaces[6] == spaces[4] == 2 and move_taken==False:
        if 2 in available_spaces_1:
            spaces[2] = 2
            move_taken = True
    if spaces[6] == spaces[2] == 2 and move_taken==False:
        if 4 in available_spaces_1:
            spaces[4] = 2
            move_taken = True
    if spaces[4] == spaces[2] == 2 and move_taken==False:
        if 6 in available_spaces_1:
            spaces[6] = 2
            move_taken = True
    if spaces[3] == spaces[4] == 2 and move_taken==False:
        if 5 in available_spaces_1:
            spaces[5] = 2
            move_taken = True
    if spaces[3] == spaces[5] == 2 and move_taken==False:
        if 4 in available_spaces_1:
            spaces[4] = 2
            move_taken = True
    if spaces[4] == spaces[5] == 2 and move_taken==False:
        if 2 in available_spaces_1:
            spaces[3] = 2
            move_taken = True
    if spaces[0] == spaces[1] == 2 and move_taken==False:
        if 2 in available_spaces_1:
            spaces[2] = 2
            move_taken = True
    if spaces[0] == spaces[2] == 2 and move_taken==False:
        if 1 in available_spaces_1:
            spaces[1] = 2
            move_taken = True
    if spaces[1] == spaces[2] == 2 and move_taken==False:
        if 0 in available_spaces_1:
            spaces[0] = 2
            move_taken = True
    if spaces[1] == spaces[4] == 2 and move_taken==False:
        if 7 in available_spaces_1:
            spaces[7] = 2
            move_taken = True
    if move_taken == False:
        def skyblock():
            global double_threat_space
            global spaces
            available_spaces_1 = available_spaces()
            print("AV: ",available_spaces_1)
            print("Looking for the block...")
            move_taken = False
            if spaces[4] == spaces[8] == 1 and move_taken==False:
                if 0 in available_spaces_1:
                    spaces[0] = 2
                    move_taken = True
            if spaces[0] == spaces[4] == 1  and move_taken==False:
                if 8 in available_spaces_1:
                    spaces[8] = 2
                    move_taken = True
            if spaces[5] == spaces[8] == 1 and move_taken==False:
                if 2 in available_spaces_1:
                    spaces[2] = 2
                    move_taken = True
            if spaces[7] == spaces[8] == 1 and move_taken==False:
                if 6 in available_spaces_1:
                    spaces[6] = 2
                    move_taken = True
            if spaces[4] == spaces[7] == 1 and move_taken==False:
                if 1 in available_spaces_1:
                    spaces[1] = 2
                    move_taken = True
            if spaces[6] == spaces[8] == 1 and move_taken==False:
                if 7 in available_spaces_1:
                    spaces[7] = 2
                    move_taken = True
            if spaces[1] == spaces[7] == 1 and move_taken==False:
                if 4 in available_spaces_1:
                    spaces[4] = 2
                    move_taken = True
            if spaces[2] == spaces[8] == 1 and move_taken==False:
                if 5 in available_spaces_1:
                    spaces[5] = 2
                    move_taken = True
            if spaces[2] == spaces[5] == 1 and move_taken==False:
                if 8 in available_spaces_1:
                    spaces[8] = 2
                    move_taken = True
            if spaces[6] == spaces[7] == 1 and move_taken==False:
                if 8 in available_spaces_1:
                    spaces[8] = 2
                    move_taken = True
            if spaces[0] == spaces[6] == 1 and move_taken==False:
                if 3 in available_spaces_1:
                    spaces[3] = 2
                    move_taken = True
            if spaces[6] == spaces[3] == 1 and move_taken==False:
                if 0 in available_spaces_1:
                    spaces[0] = 2
                    move_taken = True
            if spaces[0] == spaces[3] == 1 and move_taken==False:
                if 6 in available_spaces_1:
                    spaces[6] = 2
                    move_taken = True
            if spaces[6] == spaces[4] == 1 and move_taken==False:
                if 2 in available_spaces_1:
                    spaces[2] = 2
                    move_taken = True
            if spaces[6] == spaces[2] == 1 and move_taken==False:
                if 4 in available_spaces_1:
                    spaces[4] = 2
                    move_taken = True
            if spaces[4] == spaces[2] == 1 and move_taken==False:
                if 6 in available_spaces_1:
                    spaces[6] = 2
                    move_taken = True
            if spaces[3] == spaces[4] == 1 and move_taken==False:
                if 5 in available_spaces_1:
                    spaces[5] = 2
                    move_taken = True
            if spaces[3] == spaces[5] == 1 and move_taken==False:
                if 4 in available_spaces_1:
                    spaces[4] = 2
                    move_taken = True
            if spaces[4] == spaces[5] == 1 and move_taken==False:
                if 3 in available_spaces_1:
                    spaces[3] = 2
                    move_taken = True
            if spaces[0] == spaces[1] == 1 and move_taken==False:
                if 2 in available_spaces_1:
                    spaces[2] = 2
                    move_taken = True
            if spaces[0] == spaces[2] == 1 and move_taken==False:
                if 1 in available_spaces_1:
                    spaces[1] = 2
                    move_taken = True
            if spaces[1] == spaces[2] == 1 and move_taken==False:
                if 0 in available_spaces_1:
                    spaces[0] = 2
                    move_taken = True
            if spaces[1] == spaces[4] == 1 and move_taken==False:
                if 7 in available_spaces_1:
                    spaces[7] = 2
                    move_taken = True
            if move_taken == False:
                doubleT()
        skyblock()

def detect_win():
    #detects if a player has won. Returns the 'winner' or False
    #check diagonals
    global check1
    check1 = False
    global winner
    global spaces
    winner = 0 #a random assignment so if-else loop at end of function works
    if spaces[0] == spaces[4] == spaces[8] != 0:#if they are equal and not equal to zero (unused)
        game_over = True #win detected so game over
        winner = spaces[0] #use contents of one of spaces to identify winner
    if spaces[6] == spaces[4] == spaces[2] != 0:
        game_over = True #win detected so game over
        winner = spaces[6] #use contents of one of spaces to identify winner
#check horizontals
    for x in range (0,3): 
        start = x * 3 #displace by three for new row
        if spaces[start] == spaces[start + 1] == spaces[start + 2] != 0:#if they are equal and not equal to zero (unused)
            game_over = True #win detected so game over
            winner = spaces[start] #use contents of one of spaces to identify winner
#check verticals
    for x in range (0,3): 
        start = x #start in pos 0,1,2 (top row of grid)
        if spaces[start] == spaces[start + 3] == spaces[start + 6] != 0:
            #if they are equal and not equal to zero (unused)
            game_over = True #win detected so game over
            winner = spaces[start] #use contents of one of spaces to identify winner
        #convert winner number into text, 1 => player, 2 => computer
    if winner == 1:
        winner = 'human'
    elif winner == 2:
        winner = 'computer'
    else:
        winner = False
    return winner
###################################################
initialise()