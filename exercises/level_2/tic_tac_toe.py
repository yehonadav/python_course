import random
from IPython.display import clear_output


def display_board(board):
    clear_output()

    print('Reference Table for numbers to enter as positions: ')
    print('   |   | ')
    print(' 7 | 8 | 9 ')
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' 4 | 5 | 6 ')
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' 1 | 2 | 3 ')
    print('   |   | ')
    print('')
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'x' or marker == 'O' or marker == 'o'):
        marker = input('Player 1: Do you want to be X or O?    ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # Horizontal Bottom
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # Horizontal Middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # Horizontal Top
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # Vertical Left
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # Vertical Middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # Vertical Right
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # Diagonal Left to Right Bottom
            (board[9] == mark and board[5] == mark and board[1] == mark))  # Diagonal Right to Left Bottom


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    """check whether space on board is free"""
    return board[position] == ' '


def full_board_check(board):
    """check if entire board is full"""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    """ask player's next position (1-9)"""
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position (1 -9): ')
    return int(position)


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first')
        game_on = True

        while game_on:
            if turn == 'Player 1':
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations, PLAYER 1, you have won the game!')
                    game_on = False

                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:  # Player 2's turn
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Congratulations, PLAYER 2, you have won the game!')
                    game_on = False

                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break
