def generate_board():
    board_size = 3
    ttt_board = [["  " for x in range(board_size)] for y in range(board_size)]
    return ttt_board


def print_board(ttt_board):
    print("\n" + "=" * 18)
    print("PLAYER")
    print("=" * 18)
    print("     A    B    C")
    print(" ", "–" * 16)
    print("1 |  " + ttt_board[0][0] + "|  " + ttt_board[0][1] + "|  " + ttt_board[0][2] + "|")
    print(" ", "–" * 16)
    print("2 |  " + ttt_board[1][0] + "|  " + ttt_board[1][1] + "|  " + ttt_board[1][2] + "|")
    print(" ", "–" * 16)
    print("3 |  " + ttt_board[2][0] + "|  " + ttt_board[2][1] + "|  " + ttt_board[2][2] + "|")
    print(" ", "–" * 16)
    return


def is_cell_empty(board, row_index, column_index, player):
    # checking if coordinate is available (empty)
    if board[row_index][column_index] == "  ":
        return True
    else:
        print("It's not empty. Please enter another coordinate!")
        player_steps(board, player)
        return False
    


def player_steps(board, player):
    coordinate = list(input("Please enter coordinate: "))
    available_row_index = ["1", "2", "3"]
    available_column_index = ["a", "A", "b", "B", "c", "C"]
    # checking player input:
    while len(coordinate) != 2 or str(coordinate[1]) not in available_row_index or coordinate[0] not in available_column_index:
        print("Please enter a valid coordinate! ")
        coordinate = input()
    row_index = int(coordinate[1]) - 1
    column_dict = {"A": 0, "B": 1, "C": 2, "a": 0, "b": 1, "c": 2}
    column_index = column_dict[coordinate[0]]
    if is_cell_empty(board, row_index, column_index, player) is True:
        if player == "player1":
            board[row_index][column_index] = "X "
        if player == "player2":
            board[row_index][column_index] = "0 "
    return


def game_end(board):
    # Player 1 win condition
    for i in range(3):
        if (board[i][0] == "X " and board[i][1] == "X " and board[i][2] == "X ") or \
           (board[0][i] == "X " and board[1][i] == "X " and board[2][i] == "X ") or \
           (board[0][0] == "X " and board[1][1] == "X " and board[2][2] == "X ") or \
           (board[0][2] == "X " and board[1][1] == "X " and board[2][0] == "X "):
            print("Player 1 won!")
            exit()
    # Player 2 win condition
    for i in range(3):
        if (board[i][0] == "0 " and board[i][1] == "0 " and board[i][2] == "0 ") or \
           (board[0][i] == "0 " and board[1][i] == "0 " and board[2][i] == "0 ") or \
           (board[0][0] == "0 " and board[1][1] == "0 " and board[2][2] == "0 ") or \
           (board[0][2] == "0 " and board[1][1] == "0 " and board[2][0] == "0 "):
            print("Player 2 won!")
            exit()

    # Draw
    checkboard = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != "  ":
                checkboard += 1
    if checkboard == 9:
        print("Draw")
        exit()
    return


def main():
    board = generate_board()
    # print_board(board)
    player = "player1"
    while True:
        if player == "player1":
            print_board(board)
            player_steps(board, "player1")
            game_end(board)
            player = "player2"
        if player == "player2":
            print_board(board)
            player_steps(board, "player2")
            game_end(board)
            player = "player1"


if __name__ == '__main__':
    main()
