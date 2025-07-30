# Напишите программу, в которой описан класс. 
# У объектов класса должно быть поле, представляющее собой числовой список. 
# Этот список формируется на основе списка, переданного конструктору в качестве аргумента.
# При этом из списка-аргумента в список-поле включаются только числовые элементы (элементы других типов игнорируются). 
# Необходимо также описать метод, отображающий содержимое поля списка, 
# а также метод, вычисляющий среднее значение элементов поля списка 
# (сумма значений элементов, деленная на их количество)


class NewBornList:
    def __init__(self, list_numbers = None):
        self.list_numbers = []

        if list_numbers is None:
            list_numbers = []

        for i in list_numbers:
            if isinstance(i, (int, float)):
                self.list_numbers.append(i)

    def show(self):
        print(f"Числовой список: {self.list_numbers}")

    def aver(self):
        if not self.list_numbers:
            print("Нет чисел - нет списка")
            return None
        
        average = sum(self.list_numbers) / len(self.list_numbers)
        print(f"Среднее значение чисел списка: {average}")
        

new_list_nubmers = NewBornList([1, 2, 3, "hi", 5, "whatsUp"])

new_list_nubmers.show()
new_list_nubmers.aver()