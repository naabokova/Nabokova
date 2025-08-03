# Создайте базовый класс Vehicle (транспортное средство) с защищённым (_protected)
# атрибутом max_speed и приватным (__private) атрибутом mileage.
#  - Добавьте публичный метод display_info(), который выводит эти атрибуты.
#  - Создайте дочерний класс Bus, который наследует Vehicle и добавляет атрибут passenger_capacity.
#  - Переопределите метод display_info() в Bus, чтобы он показывал также вместимость пассажиров.


class Vehicle:
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed
        self.__mileage = mileage 

    def display_info(self):
        print(f"Max speed: {self._max_speed}" )
        print(f"Mileage: {self._Vehicle__mileage}")

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, passenger_capacity):
        super().__init__(max_speed, mileage)
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        super().display_info()
        print(f"Passenger capacity: {self.passenger_capacity}")

bus = Bus(180, 10000, 50)
bus.display_info()
