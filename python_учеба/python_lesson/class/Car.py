# Создайте класс Car. Добавьте обязательные атрибуты класса: модель, год выпуска, объем двигателя, цена, пробег, количество колес = 4.
#
# Создайте 1 экземпляр класса
#
# Создать класс наследник - Грузовик. Который, наследует все атрибуты класса, но количество колес = 8.
#
# Создать 1 экземпляр класса Наследника
#
# Добавить метод, который возвращает информацию по объекту (как в учебном видео метод description)


class Car():
    """Создаем автомобиль"""
    def __init__(self, model, year_release, volume_of_engine, price, mileage):
        """Инициализация атрибутов автомобиля - модель, год выпуска, объем двигателя, цена, пробег, количество колес"""
        self.model = model
        self.year_release = year_release
        self.volume_of_engine = volume_of_engine
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = 4
        print("Машина создана")

    def description_car(self):
        """Получение описания грузовика"""
        description = f"{self.model}, {self.year_release} года выпуска, объем двигателя {self.volume_of_engine} литра, цена - {self.price} рублей, пробег {self.mileage} километров, имеет {self.number_of_wheels} колес"
        print(f"Характеристики автомобиля: {description}")


my_new_car = Car("bmw", 2006, 2_2, 1000000, 80_000)

class Truck(Car):
    """ Представляет аспекты машины, специфические для грузовых машин"""

    def __init__(self, model, year_release, volume_of_engine, price, mileage):
        super().__init__(model, year_release, volume_of_engine, price, mileage)
        self.number_of_wheels = 8
        print("Грузовик создан")

my_truck = Truck("kamaz", 2020, 5.5, 5_000_000, 20_000)
my_truck.description_car()