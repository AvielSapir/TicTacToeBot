board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def print_board(boa):
    print("    0   1   2")
    print(f"0   {boa[0][0]} || {boa[0][1]} || {boa[0][2]} ")
    print("   ===||===||===")
    print(f"1   {boa[1][0]} || {boa[1][1]} || {boa[1][2]} ")
    print("   ===||===||===")
    print(f"2   {boa[2][0]} || {boa[2][1]} || {boa[2][2]} ")
    return None


def winner_check(boa):
    i = 0
    while i < 3:
        if boa[0][i] == boa[1][i] and boa[0][i] == boa[2][i] and boa[0][i] != " ":
            w = boa[0][i]
            return w
        i += 1

    if boa[0][0] == boa[1][1] and boa[0][0] == boa[2][2] and boa[0][0] != " ":
        w = boa[1][1]
        return w
    if boa[0][2] == boa[1][1] and boa[0][2] == boa[2][0] and boa[0][2] != " ":
        w = boa[1][1]
        return w

    i = 0
    while i < 3:
        if boa[i][0] == boa[i][1] and boa[i][0] == boa[i][2] and boa[i][0] != " ":
            w = boa[i][0]
            return w
        i += 1
    return None


def tie_check(boa):
    i = 0
    while i < 3:
        y = 0
        while y < 3:
            if boa[i][y] == " ":
                return False
            y += 1
        i += 1
    return True


def player_play(boa):
    while True:
        player_input = int(input(">: "))
        inp2 = player_input % 10
        inp1 = player_input // 10
        if inp1 > 2 or inp2 > 2:
            print("Illegal move")
            continue
        if boa[inp1][inp2] == " ":
            the_play = [inp1, inp2]
            break
        else:
            print("Illegal move")
    return the_play


def bot_ai(boa):
    if winner_check(boa) == "x":
        return -1
    if winner_check(boa) == "o":
        return 1
    if tie_check(boa):
        return 0

    best_score = -1
    i = 0
    while i < 3:
        y = 0
        while y < 3:
            if boa[i][y] == " ":
                boa[i][y] = "o"
                temp_score = player_ai(boa)
                if temp_score > best_score:
                    best_score = temp_score
                boa[i][y] = " "
            y += 1
        i += 1
    return best_score


def player_ai(boa):
    if winner_check(boa) == "x":
        return -1
    if winner_check(boa) == "o":
        return 1
    if tie_check(boa):
        return 0

    best_score = 2
    i = 0
    while i < 3:
        y = 0
        while y < 3:
            if boa[i][y] == " ":
                boa[i][y] = "x"
                temp_score = bot_ai(boa)
                if temp_score < best_score:
                    best_score = temp_score
                boa[i][y] = " "
            y += 1
        i += 1
    return best_score


def bot_play(boa):
    best_score = -2
    i = 0
    while i < 3:
        y = 0
        while y < 3:
            if boa[i][y] == " ":
                boa[i][y] = "o"
                temp_score = player_ai(boa)
                print(temp_score)
                if temp_score >= best_score:
                    best_score = temp_score
                    best_place = [i, y]
                boa[i][y] = " "
            y += 1
        i += 1
    print(f"[prediction = {best_score}]")
    return best_place


while winner_check(board) is None:
    print_board(board)
    player = player_play(board)
    if player == 0:
        board = [["x", "x", "x"],
                ["x", "x", "x"],
                ["x", "x", "x"]]
        break
    board[player[0]][player[1]] = "x"
    if winner_check(board) is not None or tie_check(board) == True:
        break
    bot = bot_play(board)
    board[bot[0]][bot[1]] = "o"
print_board(board)
the_winner = winner_check(board)
if the_winner is not None:
    print(f"{the_winner} is the winner! ")
else:
    print("it's a tie")