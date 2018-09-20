def generate_board():
    board_size = 3
    ttt_board = [["  " for x in range(board_size)] for y in range(board_size)]
    return ttt_board


def print_board(ttt_board, player):
    print("\n" + "=" * 18)
    print(player)
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


def player_steps(board, player):
    while True:
        coordinate = list(input("Please enter coordinate (e.g. a1): ").upper())
        row_index_list = ["1", "2", "3"]
        column_index_list = ["A", "B", "C"]
        # checks if input is valid:
        if len(coordinate) == 2 and coordinate[0] in column_index_list and str(coordinate[1]) in row_index_list:
            row_index = row_index_list.index(coordinate[1])
            column_index = column_index_list.index(coordinate[0])
            # checks if cell is empty:
            if board[row_index][column_index] == "  ":
                if player == "PLAYER 1":
                    board[row_index][column_index] = "X "
                else:
                    board[row_index][column_index] = "O "
                break
            else:
                print("It's not empty. Please enter another coordinate!")
                continue
        else:
            print("Please enter a valid coordinate! ")
            continue


def game_end(board, player, sign):
    # Win condition:
    for i in range(3):
        if (board[i][0] == sign and board[i][1] == sign and board[i][2] == sign) or \
           (board[0][i] == sign and board[1][i] == sign and board[2][i] == sign) or \
           (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
           (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
            print_board(board, player)
            if sign == "X ":
                print("Player 1 won!")
                exit()
            if sign == "O ":
                print("Player 2 won!")
                exit()

    # Draw
    checkboard = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != "  ":
                checkboard += 1
    if checkboard == 9:
        print_board(board, player)
        print("Draw")
        exit()
    return


def main():
    board = generate_board()
    player = "PLAYER 1"
    sign = "X "
    while True:
        print_board(board, player)
        player_steps(board, player)
        game_end(board, player, sign)
        if player == "PLAYER 1":
            player = "PLAYER 2"
            sign = "O "
            continue
        if player == "PLAYER 2":
            player = "PLAYER 1"
            sign = "X "
            continue


if __name__ == '__main__':
    main()
