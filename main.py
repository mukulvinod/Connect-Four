def print_board(board):
    for row in reversed(board):
        print(" ".join(row))
    print()

#above method actually prints the board while below one actually makes it
def initialize_board(num_rows, num_cols):
    return [['-' for _ in range(num_cols)] for _ in range(num_rows)]

def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row

#insert_chip is what puts the x and o into the board
def check_if_winner(board, col, row, chip_type):
    play = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for x, y in play:
        count = 0
        r, c = row, col

        while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == chip_type:
            count += 1
            r += x
            c += y

        r, c = row - x, col - y

        while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == chip_type:
            count += 1
            r -= x
            c -= y

        if count >= 4:
            return True

    return False

#above method is what checks to see if the board is getting filled

def main():
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    board = initialize_board(height, length)

    print_board(board)

    players = ['x', 'o']
    player_names = ['Player 1', 'Player 2']

    for i in range(2):
        print(f"{player_names[i]}: {players[i]}")

    for turn in range(height * length):
        id = turn % 2
        player = players[id]
        player_name = player_names[id]

        col = int(input(f"{player_name}: Which column would you like to choose? "))

        row = insert_chip(board, col, player)
        print_board(board)

        if check_if_winner(board, col, row, player):
            print(f"{player_name} won the game!")
            break
    else:
        print("Draw. Nobody wins.")

#this main fucntion is what runs the main code and calls the different methods

if __name__ == "__main__":
    main()