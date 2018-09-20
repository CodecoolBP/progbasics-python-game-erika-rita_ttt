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


def player_steps(board, player):
    while True:
        coordinate = list(input("Please enter coordinate (e.g. a1): ").upper())
        row_index_list = ["1", "2", "3"]
        column_index_list = ["A", "B", "C"]
        if len(coordinate) == 2:
            if coordinate[0] in column_index_list and str(coordinate[1]) in row_index_list:
                row_index = row_index_list.index(coordinate[1])
                column_index = column_index_list.index(coordinate[0])
                if board[row_index][column_index] == "  ":
                    if player == "player1":
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
        else:
            print("Please enter a valid coordinate! ")
            continue


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
        if (board[i][0] == "O " and board[i][1] == "O " and board[i][2] == "O ") or \
           (board[0][i] == "O " and board[1][i] == "O " and board[2][i] == "O ") or \
           (board[0][0] == "O " and board[1][1] == "O " and board[2][2] == "O ") or \
           (board[0][2] == "O " and board[1][1] == "O " and board[2][0] == "O "):
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



"""
def player_steps(board, player):
    available_row_index = ["1", "2", "3"]
    available_column_index = ["A", "B", "C"]
    column_dict = {"A": 0, "B": 1, "C": 2}
    while True:
        coordinate = list(input("Please enter coordinate: ").upper())
        if len(coordinate) == 2:
            if str(coordinate[1]) in available_row_index and coordinate[0] in available_column_index:
                row_index = int(coordinate[1] - 1)
                column_index = column_dict[coordinate[0]]
                if board[row_index][column_index] == "  ":
                    if player == "player1":
                        board[row_index][column_index] = "X "
                    if player == "player2":
                        board[row_index][column_index] = "0 "
                    break
                else:
                    print("It's not empty. Please enter another coordinate!")
                    continue
        else:
            print("Please enter a valid coordinate! ")
            continue     
    """

"""
    # checking player input:
    while len(coordinate) != 2 or str(coordinate[1]) not in available_row_index or coordinate[0] not in available_column_index:
        print("Please enter a valid coordinate! ")
        coordinate = input()
    """   
