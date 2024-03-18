def print_board(board):
    #print(board)
    for row in board:
        print(" | ".join(row)) #NOTE: Vertical Line
        print("-" * 9) #NOTE Horizontal Line

def check_valid_move(board, row, col):
    #print(board, row, col)
    if 0 <= row < 3 and 0 <= col < 3: #NOTE: Check if both rows and colmuns are within range
        return board[row][col] == ' ' #NOTE: checks if the specified cell on the board is empty, if not empty the move is not valid
    return False

def place_marker(board, row, col, player):
    #print(board, row, col, player)
    if check_valid_move(board, row, col): 
        board[row][col] = player #Place the players  marker if the move is valid
        return True
    else:
        return False

def check_winner(board, player):
    #TODO: Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    #TODO: Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)] #NOTE: this defines the dimesion of the board
    players = ['X', 'O'] # NOTE: this will be the marker of player
    turn = 0

    print("Welcome to Tic Tac Toe!")

    while True: # NOTE: infinite loop, which continues until a winner is determined or the game ends in a tie
        print_board(board)
        print(f"Player {players[turn]}'s turn")
        print(turn)
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if place_marker(board, row, col, players[turn]):
            if check_winner(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} wins!")
                break
            elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print_board(board)
                print("It's a tie!")
                break
            else:
                turn = (turn + 1) % 2 #NOTE: set players turn
        else:
            print("Invalid move! Try again.")


if __name__ == "__main__": # NOTE Using if __name__ == "__main__": allows you to write code that will only be executed if the script is run directly as the main program, and not if it is imported as a module into another script.
    
    main()
