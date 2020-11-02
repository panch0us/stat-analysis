# Библиотека для работы с документами .docx
import docx
# Библотека для работы с ОС
import os
# Библотека для работы с датой
import datetime
# Импортируем собсвтенный модуль для работы с файлами
import file_management

# Получаем текущий год
current_year = datetime.datetime.now().year


class Tab46_2_Years:
    """Класс для анализа текущего и прошлого года"""
    def __init__(self):
        file_path_1 = input(f'Введите путь к файлу {current_year} года: ')
        file_path_2 = input(f'Введите путь к файлу {current_year - 1} года: ')

        self.file_1 = file_management.File(name='Tab46.docx', path=file_path_1)
        self.file_2 = file_management.File(name='Tab46.docx', path=file_path_2)