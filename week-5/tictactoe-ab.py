# Tic Tac Toe with Alpha-Beta Pruning

board = [' '] * 9

def print_board():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def check_winner(p):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == p:
            return True
    return False

def is_draw():
    return ' ' not in board


# Alpha-Beta function
def alphabeta(is_max, alpha, beta):

    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = alphabeta(False, alpha, beta)
                board[i] = ' '
                
                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break   # pruning

        return best

    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = alphabeta(True, alpha, beta)
                board[i] = ' '

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break   # pruning

        return best


def best_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = alphabeta(False, -100, 100)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


# Game loop
while True:

    print_board()

    human = int(input("Enter position (0-8): "))

    if board[human] != ' ':
        print("Invalid move")
        continue

    board[human] = 'X'

    if check_winner('X'):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    ai = best_move()
    board[ai] = 'O'

    print("AI plays:", ai)

    if check_winner('O'):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break
