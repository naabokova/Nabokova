# Реализуйте класс BankAccount:
#  - Приватные атрибуты: __balance, __account_number.
#  - Геттеры для баланса и номера счёта. Сеттер только для баланса
# (с проверкой, что баланс не может быть отрицательным).
#  - Статический метод generate_account_number(), который возвращает случайный 10-значный номер счёта.
#  - Метод класса create_account(cls, initial_balance), который создаёт аккаунт с сгенерированным номером.

import random

class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError("Баланс не может быть отрицательным")
        
    @staticmethod
    def generate_account_number():
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])


    @classmethod
    def create_account(cls, initial_balance):
        if initial_balance < 0:
            raise ValueError
        account_number = cls.generate_account_number()
        return cls(initial_balance, account_number)



account = BankAccount.create_account(1000)
print(account.balance)          # 1000
account.balance = -500          # ValueError