def play(player):
    global input_
    new_y, new_x = input("Enter the coordinates: ").split()
    if not(new_y.isdigit() and new_x.isdigit()):
        print("You should enter numbers!")
    else:
        y, x = int(new_y), int(new_x)
        cell_index = 3 * (y - 1) + (x - 1)
        if not(x > 0 and x < 4 and y > 0 and y < 4):
            print("Coordinates should be from 1 to 3!")
        elif (input_ [cell_index] == "X") or (input_[cell_index] == "O"):
            print("This cell is occupied! Choose another one!")    
        else:
            input_[cell_index] = player
            print_field(input_)

def empty_field():
    return [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            
def print_field(input_):
    print("---------")
    for i in range(3):
        str_ = ""
        for j in range(3):
            str_ = str_ + input_[i * 3 + j] + " "
        print("| " + str_  + "|")
    print("---------")

def is_win_x(input_):
    win_x = False
    for i in range(3):
        if (input_[0 + i] == "X" and input_[1 + i] == "X" and input_[2 + i] == "X"):
            win_x = True
        if (input_[0 + i] == "X" and input_[3 + i] == "X" and input_[6 + i] == "X"):
            win_x = True
    if (input_[0] == "X" and input_[4] == "X" and input_[8] == "X"):
        win_x = True
    if (input_[2] == "X" and input_[4] == "X" and input_[6] == "X"):
        win_x = True
    return win_x
        
def is_win_o(input_):
    win_o = False
    for i in range(3):
        if (input_[0 + 3 * i] == "O" and input_[1 + 3 * i] == "O" and input_[2 + 3 * i] == "O"):
            win_o = True
        if (input_[0 + i] == "O" and input_[3 + i] == "O" and input_[6 + i] == "O"):
            win_o = True
    if (input_[0] == "O" and input_[4] == "O" and input_[8] == "O"):
        win_o = True
    if (input_[2] == "O" and input_[4] == "O" and input_[6] == "O"):
        win_o = True
    return win_o
               
input_ = empty_field()
print_field(input_)
player = "X"
while True:
    xs = [x for x in input_ if x == "X"]
    os = [x for x in input_ if x == "O"]
    win_x = is_win_x(input_)
    win_o = is_win_o(input_)
    if (abs(len(xs) - len(os)) > 1) or (win_x and win_o):
        print("Impossible")
        break
    else:
        if (not win_x and not win_o) and (len(xs) + len(os)) < 9:
            play(player)
        else:
            if win_x:
                print("X wins")
            elif win_o:
                print("O wins")
            else:
                print("Draw")
            break
    if player == "X":
        player = "O"
    else:
        player = "X"
