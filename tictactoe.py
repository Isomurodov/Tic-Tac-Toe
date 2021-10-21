import random
import time

def printt():
    global m
    print('---------')
    for i in m:
        print('|', ' '.join(i), '|')
    print('---------')

def result():  # after each move, this function is called to check if the game is over or whether the winner is found
    global m
    for i in range(3):
        if m[0][i] == m[1][i] == m[2][i] and m[0][i] != ' ':
            return m[0][i]
        if m[i] == ['O', 'O', 'O'] or m[i] == ['X', 'X', 'X']:
            return m[i][0]
    if (m[0][0] == m[1][1] == m[2][2] or m[0][2] == m[1][1] == m[2][0]) and m[1][1] != ' ':
        return m[1][1]

def lvl_medium():  # this function is a medium level player that can think one move ahead
    global m
    for i in range(3):
        if m[0][i] == m[1][i] and m[0][i] != ' ' and m[2][i] == ' ':
            return 2, i
        elif m[2][i] == m[1][i] and m[1][i] != ' ' and m[0][i] == ' ':
            return 0, i
        elif m[0][i] == m[2][i] and m[0][i] != ' ' and m[1][i] == ' ':
            return 1, i
        if (m[i].count('X') == 2 or m[i].count('O') == 2) and (' ' in m[i]):
            return i, m[i].index(' ')
    if m[0][0] == m[1][1] and m[1][1] != ' ' and m[2][2] == ' ':
        return 2, 2
    elif m[1][1] == m[2][2] and m[1][1] != ' ' and m[0][0] == ' ':
        return 0, 0
    elif (m[0][0] == m[2][2] and m[0][0] != ' ') and (m[0][2] == m[2][0] and m[0][2] != ' ') and m[1][1] == ' ':
        return 1, 1
    elif m[0][2] == m[1][1] and m[1][1] != ' ' and m[2][0] == ' ':
        return 2, 0
    elif m[1][1] == m[2][0] and m[1][1] != ' ' and m[0][2] == ' ':
        return 0, 2

def lvl_easy():  # randomly puts characters (either X or 0) on empty cells
    global m
    x, y = random.randint(0, 2), random.randint(0, 2)
    if m[x][y] == ' ':
        m[x][y] = symbol[0]
        return m
    else:
        lvl_easy()

def play(player):  # the central function that controls whose turn it is to play, and prompts different messages to the human players; it also calls respective functions when it is AI's turn to play
    global m, moves, end, symbol, res, win
    if player == "user":
        try:
            row, col = input('Enter the coordinates: ').split()
            row, col = int(row), int(col)
        except:
            print('You should enter numbers!')
            return play()
        if (1 <= col <= 3) and (1 <= row <= 3) and (m[row - 1][col - 1] == ' '):
            m[row - 1][col - 1] = symbol[0]
        else:
            if not ((1 <= col <= 3) and (1 <= row <= 3)):
                print('Coordinates should be from 1 to 3!')
            else:
                print('This cell is occupied! Choose another one!')
            return play("user")
    else:
        if player == "easy":
            generator()
        elif player == "medium":
            res = lvl_medium()
            if res:
                m[res[0]][res[1]] = symbol[0]
            else:
                generator()
        print(f'Making move level "{player}"')
    symbol = symbol[::-1]
    printt()
    moves += 1
    win = result()
    if win:
        end = True
        print(win, 'wins')

while True:  # putting evrything together
    try:
        inp = input('Input command: ').split()
        cmd = inp[0]
        p1, p2 = inp[1:]
    except:
        if cmd == 'exit':
            break
        print('Bad parameters!')
    else:
        moves = 0  # n. of moves
        end = False
        m = [[' ', ' ', ' '] for i in range(3)]
        symbol = ('X', 'O')
        res, win = 0, 0
        printt()
        while not end:
            play(p1)
            time.sleep(1.5)
            if (not end) and moves < 9:
                play(p2)
                time.sleep(1.5)
            if moves == 9 and not win:
                print('Draw')
                break
