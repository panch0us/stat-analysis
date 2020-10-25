# Библиотека для работы с документами .docx
import docx
# Библотека для работы с ОС
import os
# Библотека для работы с датой
import datetime

# Получаем текущий год
current_year = datetime.datetime.now().year

# Уточняем количество лет для анализа (минимум 2, максимум 5)
count_year = 1
while count_year < 2 or count_year > 5:
    # Пока текущий год меньше 2 или больше 5
    try:
        count_year = int(input('Укажите количество лет для сравнения (например 2 (доступно от 2 до 5)): '))
    except ValueError:
        print('Можно ввести только число')

def deleting_all_folders():
    """Удаляем все папки в текущей дирректории"""
    pass

def count_dir(count_year):
    """Определяем количество созаваемых папок с названиями года"""
    if count_year == 2:
        path_1 = str(current_year)
        path_2 = str(current_year - 1)

        try:
            os.mkdir(path_1)
            os.mkdir(path_2)
        except OSError:
            print('Создать 2 папки не удалось')


#document_1 = input('Укажите ')
docx = docx.Document('Tab46.docx')


if __name__ == '__main__':
    #print(f"Текущая рабочая директория {path}")
    print(docx.tables[0].rows[5].cells[0].text)