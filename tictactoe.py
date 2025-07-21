def print_board(b):
    for row in b: print("|".join(row))
    
def check_win(b, p):
    return any(
        all(cell == p for cell in row) for row in b
    ) or any(
        all(b[r][c] == p for r in range(3)) for c in range(3)
    ) or all(b[i][i] == p for i in range(3)) or all(b[i][2-i] == p for i in range(3))

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while True:
        print_board(board)
        r, c = map(int, input(f"{player} turn (row col 1–3): ").split())
        if 1 <= r <= 3 and 1 <= c <= 3 and board[r-1][c-1] == " ":
            board[r-1][c-1] = player
            moves += 1
            if check_win(board, player):
                print_board(board); print(f"{player} wins!"); break
            if moves == 9:
                print_board(board); print("It's a tie!"); break
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move, try again.")
            
if __name__ == "__main__":
    tic_tac_toe()
