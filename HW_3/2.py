# Напишите программу, в которой описан класс со следующими свойствами. 
# В классе описан конструктор, которому в качестве аргументов (помимо первой ссылки на создаваемый объект) 
# передаются текст и целое число, причем в произвольном порядке. 
# Число и текст присваиваются как значения определенным полям. 
# Если переданы два текстовых значения, то создается только текстовое поле со значением, 
# получающимся объединением значений аргументов. 
# Если аргументами переданы два числовых поля, то у объекта будет только поле с целочисленным значением, 
# равным сумме значений аргументов. 
# В иных случаях поля для объекта не создаются.
# Создать на основе класса объекты и проверить функциональность кода.  
# (Нужно вспомнить про *args и **kwargs)



class Class:
    def __init__(self, *args):
        self.text = None
        self.number = None

        if len(args) == 2:
            if isinstance(args[0], str) and isinstance(args[1], str):
                self.text = args[0] + args[1]

            elif isinstance(args[0], int) and isinstance(args[1], int):
                self.number = args[0] + args[1]

            else:
                if isinstance(args[0], str) and isinstance(args[1], int):
                    self.text = args[0]
                    self.number = args[1]
    
                elif isinstance(args[0], int) and isinstance(args[1], str):
                    self.number = args[0]
                    self.text = args[1]
    def show(self):
        info = []
        if self.text is not None:
            info.append(f"Текст: {self.text}")
        if self.number is not None:
            info.append(f"Число: {self.number}")
        print(" ".join(info) if info else "Нет данных")

obj1 = Class(1, 2)
obj1.show()

obj2 = Class("Whats", "Up")
obj2.show()

obj3 = Class(1, "One")
obj3.show()

obj4 = Class(2, "Two")
obj4.show()

obj5 = Class(0.5, (1, 2))
obj5.show()