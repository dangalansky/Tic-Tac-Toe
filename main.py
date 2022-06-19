board = ['-','-','-','-','-','-','-','-','-']
game_on = True


def print_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def check_for_win():
    global game_on
    if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[0] == board[4] ==\
            board[8] == 'X' or board[2] == board[4] == board[6] == 'X' or board[0] == board[3] == board[6] == 'X' or \
            board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X':
        print ('X WINS!')
        game_on = False
    elif board[0] == board[1] == board[2] == 'O' or board[3] == board[4] == board[5] == 'O' or board[0] == board[4] ==\
            board[8] == 'O' or board[2] == board[4] == board[6] == 'O' or board[0] == board[3] == board[6] == 'O' or \
            board[1] == board[4] == board[7] == 'O' or board[2] == board[5] == board[8] == 'O':
        print ('O WINS!')
        game_on = False
    else:
        pass

def x_turn():
    print_board()
    check_for_win()
    try:
        x_choice = int(input('Choose space (1-9) to place "X": '))
    except ValueError:
        print("Invalid Entry. Try Again.")
        x_turn()
    if x_choice:
        n = x_choice - 1
        if board[n] == '-':
            board[n] = 'X'
        else:
            print('Space is taken. Try Again.')
            x_turn()

def o_turn():
    print_board()
    check_for_win()
    try:
        o_choice = int(input('Choose space (1-9) to place "O": '))
    except ValueError:
        print("Invalid Entry. Try Again.")
        o_turn()
    if o_choice:
        n = o_choice - 1
        if board[n] == '-':
            board[n] = 'O'
        else:
            print('Space is taken. Try Again.')
            o_turn()

print('X goes first')

while game_on:
    if '-' in board:
        x_turn()
    if game_on:
        o_turn()
    else:
        game_on = False
        print('It\'s a Draw!')
