"""
Создание диаграмм, сохранение в формат картинки
"""

# Библотека для работы с датой
import datetime
# Библиотека для построения диаграмм
import matplotlib

# Получаем значение текущего года
current_year = datetime.datetime.now().year

class Diagrams:
    """Создание диаграмм"""

    def __init__(self, quantity_years=2, registered=0, solved=0, suspended=0, effectiveness=0):
        """Указываем количество зарегистрированного, раскрытого, приостановленного и раскрываемость"""
        self.quantity_years = quantity_years
        self.registered = registered
        self.solved = solved
        self.suspended = suspended
        self.effectiveness = effectiveness


    def create_diagram(self):
        """Создание столбчатой диаграммы"""
        groups = [f'{year} год' for year in range(current_year - (self.quantity_years - 1), current_year + 1)]
        counts = [self.registered, self.solved, self.suspended, self.effectiveness]
        plt.bar(groups, counts)
        plt.savefig('123.png')

    def save_diagram(self):
        pass
