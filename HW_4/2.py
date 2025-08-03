#  Создайте класс Temperature с приватным атрибутом __celsius.
#  - Реализуйте геттер и сеттер для celsius, где сеттер проверяет, 
# что температура не может быть ниже -273.15°C (абсолютный ноль).
#  - Добавьте свойство fahrenheit (геттер), 
# которое возвращает температуру в Фаренгейтах (формула: °F = °C * 9/5 + 32).


class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius


    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура должна быть не ниже -273.15 °C")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return f"self.__celsius * 9 / 5 + 32" °C


temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
temp.celsius = -100    # Должно вызвать ValueError