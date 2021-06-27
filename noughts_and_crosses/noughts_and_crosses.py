game_field = {}      # словарь, содержащий ключи - координаты ячеек и соответствующие координатам значения (X, O, -)
step = 0             # Текущий номер хода


# Декоратор для проверки правильности введённых координат ячейки
def is_correct_cell(func):  # func = input_x_o
    def wrapper():
        # Запрос координат ячейки для крестика/нолика
        if step % 2:
            print('\nКуда вы хотите поставить крестик?')
        else:
            print('\nКуда вы хотите поставить нолик?')
        
        cell_number = input('Введите номер строки и номер столбца без пробелов(например, 02): ')

        # Проверка, хочет ли игрок выйти или начать новую игру
        if cell_number == 'N':
            print('\nВы действительно хотите начать новую игру?\n')
            return start_new_game(step)
        if cell_number == 'E':
            print('\nВы действительно хотите выйти?\n')
            return start_new_game(step)

        # Проверка, существует ли такая ячейка на поле и свободна ли она.
        if cell_number in game_field.keys():
            # Если в ячейке уже есть крестик/нолик, снова запрашиваем координаты
            if game_field[cell_number] != '-': 
                print('\nЯчейка уже занята, выберите другую.')
                return input_x_o()
            else:
                # Если всё хорошо, разрешаем запись крестика/нолика по введённым координатам
                return func(cell_number)
        # если введена какая-то ересь, снова запрашиваем координаты
        else:
            print('\nВы ввели неправильное значение.')
            return input_x_o()
    return wrapper


# Функция присваивает значение Х или О ячейке поля в зависимости от номера текущего хода
@is_correct_cell
def input_x_o(cell_number='00'):
    global step
    if step % 2:
        game_field[cell_number] = "X"
    else:
        game_field[cell_number] = "O"
    step += 1

# Выводим на экран поле с новым символом
    print_game_field()


# Декоратор для определения победы или ничьей
def is_win(func):    # func = print_game_field
    def wrapper():
        func()
    # После вывода поля на экран проверяем, выиграл ли кто-нибудь

    # Делаем строки из символов в ячейках по строкам, столбцам и диагоналям
        str_1 = game_field['00'] + game_field['01'] + game_field['02']
        str_2 = game_field['10'] + game_field['11'] + game_field['12']
        str_3 = game_field['20'] + game_field['21'] + game_field['22']

        col_1 = game_field['00'] + game_field['10'] + game_field['20']
        col_2 = game_field['01'] + game_field['11'] + game_field['21']
        col_3 = game_field['02'] + game_field['12'] + game_field['22']

        diag_1 = game_field['00'] + game_field['11'] + game_field['22']
        diag_2 = game_field['02'] + game_field['11'] + game_field['20']

    # Если где-нибудь есть три крестика/нолика в ряд, завершаем игру
        if 'XXX' in [str_1, str_2, str_3,
                     col_1, col_2, col_3,
                     diag_1, diag_2]:
            print('Выиграл игрок X\n')
            return start_new_game(10)

        if 'OOO' in [str_1, str_2, str_3,
                     col_1, col_2, col_3,
                     diag_1, diag_2]:
            print('Выиграл игрок O\n')
            return start_new_game(10)

    # Если нет трёх крестиков/ноликов в ряд, а ячейки все заполнены, решаем, что ничья и заканчиваем игру.
        if '-' not in game_field.values():
            print('Ничья')
            return start_new_game(10)

    # Если ни выигрыша, ни ничьи нет, требуем заполнить новую ячейку
        else:
            input_x_o()
    return wrapper


# Вывод на экран игрового поля со всеми крестиками-ноликами
@is_win
def print_game_field():
    print('\n ', '0', '1', '2', '\n', sep='    ')
    print('0', game_field['00'], game_field['01'], game_field['02'], '\n', sep='    ')
    print('1', game_field['10'], game_field['11'], game_field['12'], '\n', sep='    ')
    print('2', game_field['20'], game_field['21'], game_field['22'], '\n', sep='    ')


# Функция, обрабатывающая решения игрока по началу и концу игры
def start_new_game(i):

    # Начало новой игры, обнуление поля и счётчика ходов (step)
    if i == 0:
        print('\n\nВы играете в крестики-нолики. Первым всегда ходит игрок с крестиками.\n')
        print('Выигрывает тот, кто первым соберёт в ряд три крестика или три нолика.\n')
        print('Вы в любой момент можете начать  новую игру, введя N или выйти, введя E.\n')

        global game_field
        game_field = dict.fromkeys(['00', '01', '02', '10', '11', '12', '20', '21', '22'], '-')
        global step
        step = 1
        print_game_field()

    # Обработка решения игрока после выигрыша/ничьей
    elif i == 10:
        while True:
            print('\nХотите начать новую игру?')
            win_new_game = input('N - начать новую игру, E - выйти из игры: ')
            if win_new_game == 'N':
                start_new_game(0)
                break
            if win_new_game == 'E':
                print('\nДо свидания. Ждём вас снова')
                break    

    # Обработка решения при незавершённой игре
    else:
        new_game = input('N - начать новую игру, E - выйти из игры, любая другая кнопка - продолжить начатую игру: ')
        if new_game == 'N':
            start_new_game(0)
        elif new_game == 'E':
            print('\nДо свидания. Ждём вас снова')
        else:
            input_x_o()


# Запуск новой игры при старте
start_new_game(0)
