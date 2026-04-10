# Simple Tic Tac Toe with Minimax

board = [' '] * 9

# Print board
def print_board():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # columns
        [0,4,8],[2,4,6]            # diagonals
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check draw
def is_draw():
    return ' ' not in board

# Minimax function
def minimax(is_max):
    
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
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)
        return best
    
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)
        return best

# Find best move for AI
def best_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            
            if score > best_score:
                best_score = score
                move = i
    return move


# Game loop
while True:
    
    print_board()
    
    # Human move
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
    
    # AI move
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
