import os


def generate_board():
    board_size = 3
    ttt_board = [["  " for x in range(board_size)] for y in range(board_size)]
    return ttt_board


def print_board(ttt_board, player):
    row_number = 1
    print("\n" + "=" * 18)
    print(player)
    print("=" * 18)
    print("     A    B    C")
    print(" ", "–" * 16)
    for i in range(3):
        print(row_number + i, "|  " + ttt_board[i][0] + "|  " + ttt_board[i][1] + "|  " + ttt_board[i][2] + "|")
        print(" ", "–" * 16)
    return


def player_steps(board, player, sign):
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
                board[row_index][column_index] = sign
                return board
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
            os.system("clear")
            print_board(board, player)
            if sign == "X ":
                print(player, "won!")
                exit()
            if sign == "O ":
                print(player, "won!")
                exit()

    # Draw
    checkboard = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != "  ":
                checkboard += 1
    if checkboard == 9:
        os.system("clear")
        print_board(board, player)
        print("Draw")
        exit()
    return


def main():
    player1 = input("Enter your name: ")
    player2 = input("Enter your name: ")
    board = generate_board()
    player = player1
    sign = "X "
    while True:
        os.system("clear")
        print_board(board, player)
        player_steps(board, player, sign)
        game_end(board, player, sign)
        if player == player1:
            player = player2
            sign = "O "
            continue
        if player == player2:
            player = player1
            sign = "X "
            continue


if __name__ == '__main__':
    main()
