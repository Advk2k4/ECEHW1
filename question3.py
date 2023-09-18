def initialize_board():
    return [str(x) for x in range(1, 10)]

def print_board(board):
    print('\n -----')
    for row in range(0, 9, 3):
        print('|' + '|'.join(board[row:row+3]) + '|')
        print(' -----')

def check_winner(board):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]

    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] == board[b] == board[c]:
            return True
    return False

def play_game():
    choices = initialize_board()
    player_one_turn = True
    play_count = 0
    winner = False

    while not winner:
        print_board(choices)

        if play_count == 9:
            print("It's a draw!")
            break

        player = "Player 1" if player_one_turn else "Player 2"
        print(f"{player}:")

        try:
            choice = int(input(">> "))
        except ValueError:
            print("Please enter a valid field.")
            continue

        if choice < 1 or choice > 9 or choices[choice - 1] == 'X' or choices[choice - 1] == 'O':
            print("Illegal move, please try again.")
            continue

        mark = 'X' if player_one_turn else 'O'
        choices[choice - 1] = mark
        play_count += 1

        if play_count >= 5 and check_winner(choices):
            winner = True
            print_board(choices)
            print(f"{player} wins!")

        player_one_turn = not player_one_turn

if __name__ == '__main__':
    play_game()
