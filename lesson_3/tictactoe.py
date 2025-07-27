import random
import os
INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
MATCHES_FOR_WIN = 5
WINNING_LINES     = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                     [1, 4, 7], [2, 5, 8], [3, 6, 9],
                     [1, 5, 9], [3, 5, 7]
                     ]

def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')   
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [key for key, value in board.items()
                     if value == INITIAL_MARKER]

def join_or(lst, sep=', ', word = 'or'):
    if not lst:
        return ''
    if len(lst) == 1:
        return str(lst[0])
    if len(lst) == 2:
        return f"{lst[0]} {word} {lst[1]}"
    
    leading_items = sep.join((str(item) for item in lst[0:-1]))
    
    return f'{leading_items}{sep}{word} {lst[-1]}'

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = int(input().strip())
        if str(square) in valid_choices:
            break
        
        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def find_at_risk_square(line, board, marker):
    #finding squares that are adjacent either for human win or computer win
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def computer_chooses_square(board):
    square = None
    #prioritize the middle square if its availible
    if board[5] == INITIAL_MARKER:
        square = 5

    #offense
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, COMPUTER_MARKER)
            if square:
                break

    #defense
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break
    

    #pick random square
    if not square:
        square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    return None

def someone_won(board):
    return bool(detect_winner(board))

def play_tic_tac_toe():
    player_count = 0
    computer_count = 0 
    TURN = random.choice(["Player", "Computer"])

    while True:
        board = initialize_board()

        while True:
            display_board(board)
            if TURN == 'Player':
                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    display_board(board)
                    break
                TURN = 'Computer'
            if TURN == 'Computer':
                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    display_board(board)
                    break
                TURN = 'Player'

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")

        if detect_winner(board) == 'Player':
            player_count += 1
        elif detect_winner(board) == 'Computer':
            computer_count += 1
        prompt(f'Player: {player_count} Computer: {computer_count}')

        if player_count == MATCHES_FOR_WIN:
            prompt("You win the match series!")
            player_count = 0
        if computer_count == MATCHES_FOR_WIN:
            prompt("The computer wins the match series!")
            computer_count = 0

        prompt('Play Again? (y or n)')
        
        answer = input().strip().lower()
        while answer == '' or answer not in ('y','n'):
            prompt("Incorrect input please enter y or n")
            answer = input().strip().lower()

        if answer[0] != 'y':
            prompt('Thanks for playing Tic Tac Toe!')
            return
play_tic_tac_toe()