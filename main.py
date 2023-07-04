map_ = list(range(1, 10))
def draw_board(map_):
   print("-" * 13)
   for i in range(3):
      print("|", map_[0+i*3], "|", map_[1+i*3], "|", map_[2+i*3], "|")
      print("-" * 13)


# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Сделать ход в ячейку
def step_map(step, symbol):
    ind = map_.index(step)
    map_[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ''

    for i in victories:
        if map_[i[0]] == 'X' and map_[i[1]] == 'X' and map_[i[2]] == 'X':
            win = 'X'
        if map_[i[0]] == 'O' and map_[i[1]] == 'O' and map_[i[2]] == 'O':
            win = 'O'

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    draw_board(map_)

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = 'X'
        step = int(input('Player 1, your turn: '))
    else:
        symbol = 'O'
        step = int(input('Player 2, your turn: '))

    step_map(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != '':
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
draw_board(map_)
print('Won', win)