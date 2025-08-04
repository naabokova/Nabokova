# Создайте базовый класс Employee с атрибутами name, 
# salary (защищённый) и методом display_info().
# От него унаследуйте Manager (добавляет атрибут department) 
# и Developer (добавляет programming_language).
# Сделайте так, чтобы salary нельзя было изменить напрямую, 
# но можно было через метод set_salary(), который проверяет, что зарплата не меньше 0.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        else:
            raise ValueError("Зарплата не может быть меньше 0")
   
    @property
    def salary(self):
        return self._salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    
dev = Developer("Alice", 5000, "Python")
dev.set_salary(-1000)  # Должно вызвать ошибку
dev.display_info()