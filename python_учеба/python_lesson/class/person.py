class Person():
    """ Модель человека"""

    def __init__(self,name, age):
        """Инициализация атрибутов человека - имя, возрас"""
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поет")


    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " танцует")


man = Person("Виталя", 42)
woman = Person("Наташа", 27)
print(man.name)

man.dance()
woman.sing()


