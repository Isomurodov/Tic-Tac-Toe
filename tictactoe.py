import random


def printt():
    global m
    print('---------')
    for i in m:
        print('|', ' '.join(i), '|')
    print('---------')


def result():
    global m, check_list
    for i in range(3):
        if m[0][i] == m[1][i] == m[2][i] and m[0][i] != ' ':
            return m[0][i]
        if m[i] == ['O', 'O', 'O'] or m[i] == ['X', 'X', 'X']:
            return m[i][0]
    if (check_list[0] == check_list[4] == check_list[8] or check_list[2] == check_list[4] == check_list[6]) and \
            check_list[4] != ' ':
        return check_list[4]

def generator():
    global m
    x, y = random.randint(0, 2), random.randint(0, 2)
    if m[x][y] == ' ':
        m[x][y] = symbol[0]
        return m
    else:
        generator()

def play(player):
    global m, moves, check_list, end, symbol
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
        generator()
        print('Making move level "easy"')
    symbol = symbol[::-1]
    printt()
    moves += 1
    check_list = [j for i in m for j in i]
    if result():
        end = True
        print(result(), 'wins')


while True:
    try:
        inp = input('Input command: ').split()
        cmd = inp[0]
        p1, p2 = inp[1:]
    except:
        if cmd == 'exit':
            exit()
        else:
            print('Bad parameters!')
            break
    moves = 0  # n. of moves
    end = False
    m = [[' ', ' ', ' '] for i in range(3)]
    symbol = ('X', 'O')
    printt()
    while not end:
        play(p1)
        if (not end) and moves < 9:
            play(p2)
        if moves == 9:
            print('Draw')
            break