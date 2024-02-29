# 2.
#     1.Створити клас Employee.
#     2.__init__ має приймати наступні аргументи: ім’я, ЗП за один робочий день.
#     3.Створити метод work(self, …) який повертає строку “I come to the office.”
#     4.Створити класи Recruiter та Developer, які наслідують клас Employee.
#     5.Перевизначити методи work в класах R та D, щоб вони повертали значення:
#       “I come to the office and start to coding.” - для Developer
#       “I come to the office and start to hiring.” - для Recruiter
#      6.Перевизначити методи __str__, щоб вони повертали строку: “Посада: Ім’я”
#      7.Зробити можливим порівнювати Employee по рівню ЗП.
#      8.Створити метод check_salary(self, days), який розраховує ЗП за передану кількість днів.
#      9. Додати в конструктор класу Developer атрибут tech_stack (список з назвами технологій).
#      10.Для класу Developer зробити порівняння за кількістю технологій.
#      11.Зробити можливим операцію додавання об’єктів класу Developer.
#        Результатом має бути новий об’єкт, в якому name = name1 + ‘ ’ + name2,
#      a tech_stack - список з технологій двох об’єктів (тільки унікальні значення), ЗП - більша з двох


# 3.
# Додати до класу Employee методи save_email(self) та validate_email(self, email) та атрибут email
# Створити виняток EmailAlreadyExistsException
# Метод save_email має викликатись в кінці методу __init__ та записувати email в файл emails.csv
# Метод validate_email має перевіряти чи існує імейл в файлі. Якщо імейл вже існує, то викликати помилку EmailAlreadyExistsException




import csv, os

class EmailAlreadyExistsException(Exception):
    pass

class Employee:
    def __init__(self, name, salary_aday, email) -> None:
        self.name = name
        self.salary_aday = salary_aday
        self.email = email
        self.validate_email(email)
        self.save_email()

    def work(self):
        return "I come to the office."

    def __eq__(self, other):
        return self.salary_aday == other.salary_aday

    def __lt__(self, other):
        return self.salary_aday < other.salary_aday

    def __gt__(self, other):
        return self.salary_aday > other.salary_aday

    def __ne__(self, other):
        return self.salary_aday != other.salary_aday

    def check_salary(self, days):
        return self.salary_aday * days
    
    def validate_email(self, email):
        if not os.path.exists('emails.csv'):
            return
        
        exists = False
        with open('emais.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for item in reader:
                if email in item:
                    exists = True
                    break
        
        if exists:
            raise EmailAlreadyExistsException

    
    def save_email(self):    
        with open('emails.csv', 'a' ,newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.email])



class Recrutier(Employee):
    def __init__(self, name, salary_aday, email) -> None:
        super().__init__(name, salary_aday, email)

    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self) -> str:
        return f"Recrutier: {self.name}"


class Developer(Employee):
    def __init__(self, name, salary_aday, email, tech_stack) -> None:
        super().__init__(name, salary_aday, email)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start to coding."

    def __str__(self) -> str:
        return f"Developer: {self.name}"

    def __eq__(self, other):
        return len(self.tech_stack) == len(self.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(self.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(self.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(self.tech_stack)

    def __add__(self, other):
        return Developer(f"{self.name} {other.name}",
                         max(self.salary_aday, other.salary_aday),
                         list(set(self.tech_stack + other.tech_stack)))


