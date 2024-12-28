import math

# Initialize the board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Function to print the board
def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if there are moves left
def is_moves_left():
    for row in board:
        if ' ' in row:
            return True
    return False

# Function to evaluate the board for a winner
def evaluate():
    # Check rows and columns for winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return 10 if row[0] == 'X' else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 10 if board[0][2] == 'X' else -10

    # No winner
    return 0

# Minimax algorithm
def minimax(depth, is_maximizing):
    score = evaluate()

    # If the game is over, return the score
    if score == 10 or score == -10:
        return score
    if not is_moves_left():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # AI move
                    best = max(best, minimax(depth + 1, False))
                    board[i][j] = ' '  # Undo move
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # Opponent move
                    best = min(best, minimax(depth + 1, True))
                    board[i][j] = ' '  # Undo move
        return best

# Find the best move for AI
def find_best_move():
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'  # AI move
                move_val = minimax(0, False)
                board[i][j] = ' '  # Undo move
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Main function
if __name__ == "__main__":
    print("Tic-Tac-Toe Game!")
    print_board()

    while is_moves_left():
        # Player (O) makes a move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move! Try again.")
            continue

        # Check if player wins
        if evaluate() == -10:
            print("You win!")
            print_board()
            break

        # AI (X) makes a move
        print("AI is making a move...")
        best_move = find_best_move()
        if best_move != (-1, -1):
            board[best_move[0]][best_move[1]] = 'X'

        print_board()

        # Check if AI wins
        if evaluate() == 10:
            print("AI wins!")
            break

    if evaluate() == 0 and not is_moves_left():
        print("It's a draw!")
