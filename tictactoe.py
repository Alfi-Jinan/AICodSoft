import math

EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_board_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    else:
        return 0

# Function to perform minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth+1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth+1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[EMPTY]*3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while not is_board_full(board):
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        if board[row][col] != EMPTY:
            print("Invalid move! That spot is already taken.")
            continue
        board[row][col] = PLAYER_O
        print_board(board)
        if check_winner(board, PLAYER_O):
            print("Congratulations! You win!")
            return
        if is_board_full(board):
            print("It's a draw!")
            return
        # AI's move
        print("AI is thinking...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = PLAYER_X
        print("AI's move:")
        print_board(board)
        if check_winner(board, PLAYER_X):
            print("AI wins!")
            return
        if is_board_full(board):
            print("It's a draw!")
            return

if __name__ == "__main__":
    play_game()
