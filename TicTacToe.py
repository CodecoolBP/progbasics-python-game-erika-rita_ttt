def generate_board():
    board_size = 3
    ttt_board = [["  " for x in range(board_size)] for y in range(board_size)]
    # print(ttt_board)
    return ttt_board


def print_board(ttt_board):
    print("     A    B    C")
    print(" ", "–" * 16)
    # for i in range(board_size):
    print("1 |  " + ttt_board[0][0] + "|  " + ttt_board[0][1] + "|  " + ttt_board[0][2] + "|")
    print(" ", "–" * 16)
    print("2 |  " + ttt_board[1][0] + "|  " + ttt_board[1][1] + "|  " + ttt_board[1][2] + "|")
    print(" ", "–" * 16)
    print("3 |  " + ttt_board[2][0] + "|  " + ttt_board[2][1] + "|  " + ttt_board[2][2] + "|")
    print(" ", "–" * 16)
    return


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
    # checking if coordinate is available (empty)
    if board[row_index][column_index] == "  ":
        if player == "player1":
            board[row_index][column_index] = "X "
        if player == "player2":
            board[row_index][column_index] = "0 "
    else:
        print("It's not empty. Please enter another coordinate!")
        player_steps(board, player)
    return coordinate


def win_condition(board):
    pass


def game_end():
    pass


def main():
    board = generate_board()
    # print_board(board)
    player = "player1"
    while True:
        if player == "player1":
            print("\n" + "=" * 18)
            print("PLAYER 1")
            print("=" * 18)
            print_board(board)
            player_steps(board, "player1")            
            win_condition(board)
            player = "player2"
        if player == "player2":
            print("\n" + "=" * 18)
            print("PLAYER 2")
            print("=" * 18)
            print_board(board)
            player_steps(board, "player2")
            win_condition(board)
            player = "player1"
        game_end()
    pass


if __name__ == '__main__':
    main()