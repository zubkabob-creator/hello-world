def create_board():
    """Создаем пустое игровое поле"""
    return [[' ' for _ in range(3)] for _ in range(3)]


def print_board(board):
    """Выводим текущее состояние поля"""
    print('   0   1   2')
    for i, row in enumerate(board):
        print(f'{i}  {" | ".join(row)}')
        if i != len(board) - 1:
            print('  ---+---+---')


def is_valid_move(x, y, board):
    """Проверяем корректность выбранного места на поле"""
    try:
        x = int(x)
        y = int(y)
        if not (0 <= x < 3 and 0 <= y < 3):
            raise ValueError("Координаты неверны")
        elif board[x][y] != ' ':
            raise ValueError("Эта клетка уже занята")
        else:
            return True
    except ValueError as e:
        print(e)
        return False


def check_winner(board):
    """Определяем победителя или его отсутствие"""
    # Проверка строк и столбцов
    for i in range(3):
        if all([cell == 'X' for cell in board[i]]) or all([row[i] == 'X' for row in board]):
            return 'X'
        if all([cell == 'O' for cell in board[i]]) or all([row[i] == 'O' for row in board]):
            return 'O'

    # Проверка диагоналей
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    if all(cell == 'X' for cell in diag1) or all(cell == 'X' for cell in diag2):
        return 'X'
    if all(cell == 'O' for cell in diag1) or all(cell == 'O' for cell in diag2):
        return 'O'

    # Если победитель не найден
    return None


def play_game():
    """Основной цикл"""
    board = create_board()
    current_player = 'X'
    while True:
        print_board(board)
        print(f"\nХодит {current_player}. Введите координаты (строка столбец): ")
        move = input().strip().split()  # Получаем строку и столбец

        if len(move) != 2 or not is_valid_move(*move, board):
            continue

        x, y = map(int, move)
        board[x][y] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Победил {winner}!")
            break

        # Переключаемся на другого игрока
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()








