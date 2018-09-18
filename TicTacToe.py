def generate_board(board_size):
    ttt_board = [["  " for x in range(board_size)] for y in range(board_size)]
    # print(ttt_board)
    return ttt_board


def print_board(board_size, ttt_board):
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


def player1_steps():
    #coordinate = list(input("Please enter coordinate: "))
    pass


def player2_steps():
    pass


def win_condition():
    pass


def game_end():
    player1_steps


def main():
    board_size = 3
    board = generate_board(board_size)
    print_board(board_size, board)
    player = 1
    while True:
        if player == 1:
            player1_steps()
            win_condition()
            player = 2
        if player == 2:
            player2_steps()
            win_condition()
            player = 1
        game_end()
    pass


if __name__ == '__main__':
    main()