def convert(move):
    sx = ord(move[0]) - ord("a") + 1
    sy = abs(int(move[1]) - 8)
    ex = ord(move[3]) - ord("a") + 1
    ey = abs(int(move[4]) - 8)
    return sx, sy, ex, ey

def move_rook(board, sx, sy, ex, ey):
    for i in range(abs(sx - ex) - 1):
        if board[sy][]



if input("standart/custom") == "standart":
    board = [['BR', 'Bk', 'BB', 'BQ', 'BK', 'BB', 'Bk', 'BR']
             ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP']
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
             ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP']
             ['WR', 'Wk', 'WB', 'WQ', 'WK', 'WB', 'Wk', 'WR']]
input = 0
turn = "white"
while input != "endgame":

    if playerturn == "White":
        print("White to move")
    else:
        print("Black to move")

    input = str(input())
    if input != endgame:
        sx, sy, ex, ey = covert(input)
        stile = board[sy][sx]
        etile = board[ey][ex]

        if stile != 'E':
            if stile[0] == playerturn[0]:
                if stile[1] == "R":
                    if sx == ex ^ sy == ey and

                elif stile[1] == "k":


                elif stile[1] == "B":


                elif stile[1] == "Q":


                elif stile[1] == "K":


            else:
                print("move unavailable")
        else:
            print("move unavailable")
