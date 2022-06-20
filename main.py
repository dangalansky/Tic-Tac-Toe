from random import randint

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
x_score = 0
o_score = 0
game_over = False

def score_board():
    global x_score
    global o_score
    print('-------------------------------')
    print(f'----------X Score: {x_score}-----------')
    print(f'----------O Score: {o_score}-----------')
    print('-------------------------------')


def print_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def check_for_draw():
    global game_over
    global board
    if not '-' in board:
        print('Game over! It\'s A Draw!')
        again = input('Would you like to play again? Y or N: ')
        if again.lower() == 'y':
            board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
            game_on()
        else:
            game_over = True
            print('Final Score:')
            score_board()



def check_for_win():
    global game_over, board, x_score, o_score
    if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[0] == board[4] == \
            board[8] == 'X' or board[2] == board[4] == board[6] == 'X' or board[0] == board[3] == board[6] == 'X' or \
            board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X':
        x_score += 1
        print('\nX WINS!')
        again = input('Would you like to play again? Y or N: ')
        if again.lower() == 'y':
            board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
            game_on()
        else:
            game_over = True
            print('Final Score:')
            score_board()
    if board[0] == board[1] == board[2] == 'O' or board[3] == board[4] == board[5] == 'O' or board[0] == board[4] == \
            board[8] == 'O' or board[2] == board[4] == board[6] == 'O' or board[0] == board[3] == board[6] == 'O' or \
            board[1] == board[4] == board[7] == 'O' or board[2] == board[5] == board[8] == 'O':
        o_score += 1
        print('\nO WINS!')
        again = input('Would you like to play again? Y or N: ')
        if again.lower() == 'y':
            board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
            game_on()
        else:
            game_over = True
            print('Final Score:')
            score_board()


def x_turn():
    global game_over
    print_board()
    check_for_win()
    check_for_draw()
    if not game_over:
        try:
            x_choice = int(input('Choose space (1-9) to place "X": '))
            n = x_choice - 1
            if board[n] == '-':
                board[n] = 'X'
            else:
                print('Space is taken. Try Again.')
                x_turn()
        except (ValueError, IndexError):
            print("Invalid Entry. Try Again.")
            x_turn()


def o_turn():
    global game_over
    print_board()
    check_for_win()
    check_for_draw()
    if not game_over:
        try:
            o_choice = int(input('Choose space (1-9) to place "O": '))
            n = o_choice - 1
            if board[n] == '-':
                board[n] = 'O'
            else:
                print('Space is taken. Try Again.')
                o_turn()
        except (ValueError, IndexError):
            print("Invalid Entry. Try Again.")
            o_turn()


def game_on():
    score_board()
    number = randint(0,1)
    if number == 1:
        print('X Goes First')
    else:
        print('0 Goes First')
    while not game_over:
        if number == 1:
            x_turn()
            o_turn()
        else:
            o_turn()
            x_turn()

game_on()
