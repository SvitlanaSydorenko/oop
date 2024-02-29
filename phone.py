# 1. Описуємо телефон:

# Клас телефону.

# У нього мають бути:
# Поле для опису номера
# Метод, щоб задати номер телефону
# Захищене поле для лічильника вхідних дзвінків
# Метод, який поверне нам кількість прийнятих дзвінків
# Метод прийняти дзвінок, який додає до лічильника одиницю
# Створіть три різні об’єкти телефону. Поміняйте всім початковий номер. Прийміть по кілька дзвінків на кожному (різна кількість)

# Напишіть функцію, яка приймає список з об’єктів телефонів, а повертає загальну кількість прийнятих дзвінків з усіх телефонів.
# * Зберігати інформацію про прийняті дзвінки у файл (txt або краще csv)

import random
import csv


class Phone:
    def __init__(self, number=None) -> None:
        self.number = number
        self.__income_counter = 0

    def set_number(self, number):
        self.number = number

    def get_income_counter(self):
        return self.__income_counter

    def accept_call(self):
        self.__income_counter += 1


def func(phones):

    with open('report.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Номер', 'Кільксть вхідних'])

        counter = 0
        for phone in phones:
            counter += phone.get_income_counter()
            csv_writer.writerow([phone.number, phone.get_income_counter()])
        
        csv_writer.writerow(['Загалом', counter])

    return counter


def main():

    phones = [Phone(), Phone(), Phone()]

    for phone in phones:
        number = '(067)' + ''.join([str(random.randint(0, 9)) for x in range(7)])
        phone.set_number(number)
    
        for i in range(random.randint(5, 10)):
            phone.accept_call()

    func(phones)


if __name__ == "__main__":
    main()
