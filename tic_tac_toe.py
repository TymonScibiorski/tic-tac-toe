print("Welcome to tic tac toe (you can stop the game at any time by writing 'break' or by simply pressing CTRL+C)")
print("What table size would you like?")
print("[3] - 3x3 \n[4] - 4x4")
# print("\n")

#builds the table in the variable table
def buildTable():
    table = []
    y = -1
    for i in range(dimentions):
        table.append([])
        for z in range(dimentions):
            table[i].append([y+1])
            y += 1

    return table

#prints the table in a nice fashion, otherwise it would look like this (uncomment if you wanna see how it would like without it):
#print(table)
def tablePrint():
    y = 0
    for i in range(len(table)):
        for char in table[i]:
            if (y+1) % dimentions == 0:
                print(char)    
            else:
                print(char, end="\t")
            y += 1
            
#gets the coordinates. from the user, to the program
def coor_get(num):
    x = num % dimentions
    y = num / dimentions
    return x, int(y)




wnst = False #won/lost
i = 0


while wnst == False:
    dimentions = int(input(":"))
    table = buildTable()
    if dimentions == "break":
        break
    while wnst == False:
        if i != 0:
            print("\n")
        tablePrint() #prints the table
        
        if i % 2 == 0: #checks if the move's number is even or not. If it is, the symbol is X, otherwise it's O
            move = "X"
        else:
            move = "O"

        #takes the input from the user
        print("Where would you like to place the next move? " + "(Which is " + move + ") ") 
        ui = input()
        
        #reacts to the command "break"
        if ui == "break":
            wnst = True

        #sets the correct place in a table for X or O

        if type(table[coor_get(int(ui))[1]][coor_get(int(ui))[0]]) != str:
            table[coor_get(int(ui))[1]][coor_get(int(ui))[0]] = move
            i += 1
        else:
            print("occupado, try again")
        
        #horisontal winning
        if dimentions == 4: #four by four table
            for y in range(dimentions - 1):
                if table[y][0] == table[y][1] == table[y][2] == table[y][3] and type(table[y][0]) != int:
                    tablePrint()
                    print(move + " won!")
                    wnst = True
        else: #three by three table
            for y in range(dimentions):
                if table[y][0] == table[y][1] == table[y][2] and type(table[y][0]) != int:
                    tablePrint()
                    print(move + " won!")
                    wnst = True


        #vertical winning
        if dimentions == 4:
            for y in range(dimentions - 1):
                if table[0][y] == table[1][y] == table[2][y] == table[3][y] and type(table[0][y]) != int:
                    tablePrint()
                    print(move + " won!")
                    wnst = True
        else:
            for y in range(dimentions - 1):
                if table[0][y] == table[1][y] == table[2][y] == table[3][y] and type(table[0][y]) != int:
                    tablePrint()
                    print(move + " won!")
                    wnst = True

        #across winning
        if dimentions == 4:
            if table[0][0] == table[1][1] == table[2][2] == table[3][3] and type(table[0][0]) != int:
                tablePrint()
                print(move + " won!")
                wnst = True
            if table[0][3] == table[1][2] == table[2][1] == table[3][0] and type(table[0][3]) != int:
                tablePrint()
                print(move + " won!")
                wnst = True
        else:
            if table[0][0] == table[1][1] == table[2][2] and type(table[0][0]) != int:
                tablePrint()
                print(move + " won!")
                wnst = True
            if table[0][2] == table[1][1] == table[2][0] and type(table[0][2]) != int:
                tablePrint()
                print(move + " won!")
                wnst = True
        
        #tie
        if i == (dimentions**2):
            print("Tie")
            wnst = True