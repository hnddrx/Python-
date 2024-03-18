def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))
        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            if is_board_full(board):
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()