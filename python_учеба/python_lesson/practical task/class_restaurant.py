# Создать класс с именем Restaurant, класс должен содержать два атрибута
# имя ресторана - restaurant_name
# тип кухни - cuisine_type

# Создайте метод describe_restaurant() который выводит два атрибута и и метод open_restaurant()
#  который выводит сообщение о том, что ресторан открыт



class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализируем атрибуты - имя рестарана и тип кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        print("Модель ресторана создана")

    def describe_restaurant(self):
        print(f"Имя ресторана в который мы сегодня пойдем называется {self.restaurant_name}")
        print(f"Кухня в этом ресторане - {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт")

class IceCreamStand(Restaurant):
    """Представляет разновидность ресторана"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def varieties_flavors(self):
        """Выводит список разновидностей мороженого"""
        for flavors in self.flavors:
            print(f"Мороженое бывает: {flavors} ")


icecream = IceCreamStand("Gelatto", "десерты", ["клубничное", "шоколадное", "фруктовый лед", "ванильное"])
icecream.varieties_flavors()


# restaurant = Restaurant("Римские каникулы", "итальянская")
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# favorite_restaurant = Restaurant("Ланин", "русская")
# terrible_restaurant = Restaurant("У тети Любы", "европейская")
# family_restaurant = Restaurant("Пирожковая", "русская")
#
# favorite_restaurant.describe_restaurant()
# terrible_restaurant.describe_restaurant()
# family_restaurant.describe_restaurant()

