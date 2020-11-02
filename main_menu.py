print('*** АНАЛИЗ ФАЙЛОВ СТАТИСТИКИ ИЦ ***\n\n'
      'Меню Программы:\n'
      '\t1. Tab46\n'
      '\t2. ...\n'
      '')

user_selection = 0
while user_selection < 1:
    try:
        user_selection = int(input('Введите номер файла для анализа: '))
    except ValueError:
        print('Можно вводить только числа!')

if user_selection == 1:
    pass
