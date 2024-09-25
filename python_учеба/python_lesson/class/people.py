class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100


    def description_person(self):
        """Получение описания человека"""
        description = f"{self.name}, ему {self.age} лет, его рост {self.height}, его вес {self.weight}"
        print(f"Нового человека зовут: {description}")

    def get_weight(self):
        """Получение веса человека"""
        print(f"Вес нашего человека {self.weight}")

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс война"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Заряд ярости человека"""
        print(f"Заряд ярости нашего человека: {self.rage}")

    def description_person(self):
        """Переопределение метода родителя"""
        description = f"{self.name}, ему {self.age} лет, его заряд ярости {self.rage}"
        # print(f"Нового человека зовут: {description}")
        return  description




warrior = Warrior("Вася", 30,200)
warrior.update_weight(150)
warrior.get_rage()
print(f"Нового человека зовут: {warrior.description_person()}")


man = Person("Вася", 30,176)
# man.weight = 78
man.description_person()
# man.update_weight(110)
# man.get_weight()
