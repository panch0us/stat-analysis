# Библиотека для работы с документами .docx
import docx


class File:
    """Путь к файлу"""

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.document = docx.Document(self.path + '\\' + self.name)

    def __repr__(self):
        return f"Имя файла:\t\t{self.name}\n" \
               f"Путь к файлу:\t{self.path}\n"