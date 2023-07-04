print('welcome to tic-tac-toe')
print('-----> rules <-----')
print('  input format: a b')
print('a - line number')
print('b - column number')
print('')
print('!!!enjoy the game!!!')

def draw_board():
    print('  --------------- ')
    print('    | 0 | 1 | 2 | ')
    print('  --------------- ')
    for i, row in enumerate(board):
        row_str = f'  {i} | { " | ".join(row)} | '
        print(row_str)
        print('  --------------- ')
    print()

def step_board():
    while True:
        step = input('         Your step is: ').split()
        if len(step) != 2:
            print('Input two numbers!')
            continue

        a, b = step

        if not (a.isdigit()) or not (b.isdigit()):
            print('Input numbers!')
            continue

        a, b = int(a), int(b)

        if 0 > a or a > 2 or 0 > b or b > 2:
            print('Step is out of range!')
            continue

        if board[a][b] != ' ':
            print('The cell is already busy!')
            continue

        return a, b


def get_result():
    victories = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for step in victories:
        symbols = []
        for j in step:
            symbols.append(board[j[0]][j[1]])
        if symbols == ['X', 'X', 'X']:
            print('X won')
            return True
        if symbols == ['0', '0', '0']:
            print('0 won')
            return True
    return False

board = [[' '] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    draw_board()
    if count % 2 == 1:
        print(' X turn!')
    else:
        print(' 0 turn!')

    a, b = step_board()

    if count % 2 == 1:
        board[a][b] = 'X'
    else:
        board[a][b] = '0'

    if get_result():
        print('---game over---')
        break

    if count == 9:
        print('---game over---')
        print(' Draw!')
        break