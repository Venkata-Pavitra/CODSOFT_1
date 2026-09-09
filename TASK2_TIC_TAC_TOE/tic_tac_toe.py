import math
board = [" " for _ in range(9)]
HUMAN = "X"
AI = "O"
def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()
def check_winner():
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None
def minimax(depth, maximizing_player, alpha, beta):
    result = check_winner()
    if result == AI:
        return 10 - depth
    if result == HUMAN:
        return depth - 10
    if result == "Draw":
        return 0
    if maximizing_player:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(
                    depth + 1,
                    False,
                    alpha,
                    beta
                )
                board[i] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(
                    depth + 1,
                    True,
                    alpha,
                    beta
                )
                board[i] = " "
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score
def get_best_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(
                0,
                False,
                -math.inf,
                math.inf
            )
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please enter a number from 1 to 9.")
            elif board[move] != " ":
                print("That position is already occupied.")
            else:
                board[move] = HUMAN
                break
        except ValueError:
            print("Please enter a valid number.")
def ai_move():
    print("AI is thinking...")
    move = get_best_move()
    if move is not None:
        board[move] = AI
def play_game():
    print("\n==============================")
    print("      TIC-TAC-TOE AI")
    print("==============================")
    print("You are X")
    print("AI is O")
    print("Choose positions using 1-9:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    while True:
        print_board()
        human_move()
        result = check_winner()
        if result is not None:
            print_board()
            if result == HUMAN:
                print("🎉 Congratulations! You won!")
            else:
                print("It's a draw!")
            break
        ai_move()
        result = check_winner()
        if result is not None:
            print_board()
            if result == AI:
                print("🤖 AI wins! Better luck next time.")
            else:
                print("It's a draw!")
            break
if __name__ == "__main__":
    play_game()