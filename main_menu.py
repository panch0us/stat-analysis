# Библотека для работы с датой
import datetime
# Импортируем собсвтенный модуль для работы с файлами
import file_management


print('*** АНАЛИЗ ФАЙЛОВ СТАТИСТИКИ ИЦ ***\n\n'
      'Меню Программы:\n'
      '\t1. Tab46\n'
      '\t2. ...\n')


# Выбираем пункт меню, можно только цифры
user_selection = 0
while user_selection < 1:
    try:
        user_selection = int(input('Введите номер файла для анализа: '))
    except ValueError:
        print('Можно ввести только число!')

# Выбираем количество лет для сравнения

# Получаем текущий год
current_year = datetime.datetime.now().year

# Уточняем количество лет для анализа (минимум 2, максимум 5)
count_year = 1
while count_year < 2 or count_year > 5:
    # Выполняется пока текущий год меньше 2 или больше 5
    try:
        count_year = int(input('Укажите количество лет для сравнения (доступно от 2 до 5)): '))
    except ValueError:
        print('Можно ввести только число!')

# Если выбран № 1 в главном меню
if user_selection == 1:
    # Если выбрано 2 года для анализа:
    if count_year == 2:
        print(f'\nВы выбрали № 1 в меню и 2 года для анализа\n')

        file_path_1 = input(f'Введите путь к файлу {current_year} года: ')
        file_path_2 = input(f'Введите путь к файлу {current_year - 1} года: ')

        file_1 = file_management.File(name='Tab46.docx',
                                      path=file_path_1)
        file_2 = file_management.File(name='Tab46.docx',
                                      path=file_path_2)
        print(file_1.document.tables[0].rows[5].cells[0].text)
        print(file_2.document.tables[0].rows[5].cells[0].text)

# C:\Users\panchous\Desktop\home\data_python\2019\09_2019\ur