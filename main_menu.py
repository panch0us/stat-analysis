# Библотека для работы с датой
import datetime
# Импортируем собсвтенный модуль для работы с файлом Tab46.docx
import tab46


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

        # Вызываем класс для обработки двух лет из модуля tab46.py
        tab46.Tab46_2_Years()


# C:\Users\panchous\Desktop\home\data_python\2019\09_2019\ur
# C:\Users\panchous\Desktop\home\data_python\2020\09_2020\ur