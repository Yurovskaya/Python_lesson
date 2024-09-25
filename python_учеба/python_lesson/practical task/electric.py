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

    # # Определение атрибутов и методов класса-потомка
    #     self.battery_size = 75


class Battery():
    """Простая модель аккумулятора электромобиля"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"Мощность батарее у этой машины {self.battery_size}-kwh")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 75:
            range = 200
        elif self.battery_size == 100:
            range = 315
        print(f"Этот автомобиль может проехать около {range} миль на полной зарядке")



class ElectricCar(Car):
    """ Представляет аспекты машины, специфические для электомобилей"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя"""
        super().__init__(make, model, year)
        # Экземпляры как атрибуты
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()