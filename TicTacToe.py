def generate_board():
    board_size = 3
    ttt_board = [["  " for x in range(board_size)] for y in range(board_size)]
    # print(ttt_board)
    return ttt_board


def print_board(ttt_board):
    print("\n     A    B    C")
    print(" ", "–" * 16)
    # for i in range(board_size):
    print("1 |  " + ttt_board[0][0] + "|  " + ttt_board[0][1] + "|  " + ttt_board[0][2] + "|")
    print(" ", "–" * 16)
    print("2 |  " + ttt_board[1][0] + "|  " + ttt_board[1][1] + "|  " + ttt_board[1][2] + "|")
    print(" ", "–" * 16)
    print("3 |  " + ttt_board[2][0] + "|  " + ttt_board[2][1] + "|  " + ttt_board[2][2] + "|")
    print(" ", "–" * 16)
    return


def player1_steps(board):
    coordinate = list(input("Please enter coordinate: "))  # TODO: check if coordinates are available
    row_index = int(coordinate[1]) - 1
    column_dict = {"A": 0, "B": 1, "C": 2, "a": 0, "b": 1, "c": 2}
    column_index = column_dict[coordinate[0]]
    board[row_index][column_index] = "X"
    print_board(board)
    return


def player2_steps(board):
    coordinate = list(input("Please enter coordinate: "))  # TODO: check if coordinates are available
    row_index = int(coordinate[1]) - 1
    column_dict = {"A": 0, "B": 1, "C": 2, "a": 0, "b": 1, "c": 2}
    column_index = column_dict[coordinate[0]]
    board[row_index][column_index] = "0"
    print_board(board)
    return


def win_condition(board):
    pass


def game_end():
    player1_steps


def main():
    board = generate_board()
    print_board(board)
    player = 1
    while True:
        if player == 1:
            print("PLAYER 1")
            player1_steps(board)
            win_condition(board)
            player = 2
        if player == 2:
            print("PLAYER 2")
            player2_steps(board)
            win_condition(board)
            player = 1
        game_end()
    pass


if __name__ == '__main__':
    main()