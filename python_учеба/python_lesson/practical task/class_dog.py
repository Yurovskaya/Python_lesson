class Dog():
     """Модель собаки"""
     def __init__(self, name, age):
         """Инициализирует атрибуты - имя и возраст """
         self.name = name
         self.age = age
         print("Модель собаки создана")

     def sid(self):
         """Собака садится по команде"""
         print(f"{self.name} сейчас сидит")

     def roll_over(self):
         """Собака перекатывается по команде"""
         print(f"{self.name} перевернулась")

my_dog = Dog("Эльба", 12)

my_dog.sid()
my_dog.roll_over()

print(f"Имя моей собаки {my_dog.name}")

your_dog = Dog("Бобик", 5)
print(f"Имя твоей собаки {your_dog.name}")
print(f"Твей собаке {your_dog.age} лет")
your_dog.sid()