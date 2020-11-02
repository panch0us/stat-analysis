class File:
    """Путь к файлу"""

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __repr__(self):
        return f"Имя файла:\t\t{self.name}\nПуть к файлу:\t{self.path}"
