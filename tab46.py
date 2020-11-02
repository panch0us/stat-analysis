# Библиотека для работы с документами .docx
import docx
# Библотека для работы с ОС
import os
# Библотека для работы с датой
import datetime
# Импортируем собсвтенный модуль для работы с файлами
import file_management




# document_1 = input('Укажите ')
# docx = docx.Document('Tab46.docx')



if __name__ == '__main__':
    # print(f"Текущая рабочая директория {path}")
    print()
    # print(docx.tables[0].rows[5].cells[0].text)
    file_path = file_management.File(name='Tab46.docx',
                                     path='C:/Users/panchous/Desktop/home/data_python/2020/09_2020/ur')
    print(file_path)
