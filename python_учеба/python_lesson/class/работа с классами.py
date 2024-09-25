# Работа с классами и экземплярами

class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализируем атрибуты класса"""
        self.make = make
        self.model = model
        self.year = year
        #  Назначение атрибуту значения по умолчанию
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины"""
        print(f"Пробег машины {self.odometer_reading} в милях")

    # Изменение значения атрибута с помощью метода

    def update_odometer(self, mileage):
            """Устанавливает заданное значение на одометре"""
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("Недопустимо скручивать значение одометра. Введенное значение меньше текущего.")

   # Изменение значение атрибутов с приращением
    def increment_odometr(self, mileage):
        """Увеличение показания одометра с заданным приращением"""
        self.odometer_reading += mileage


my_new_car = Car( "audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
my_new_car.increment_odometr(100)
my_new_car.read_odometer()

# Изменение значений атрибутов

# # Прямое изменение значения атрибута
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()



