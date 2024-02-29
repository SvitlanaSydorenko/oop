# 4.  Створити клас Candidate
# В __init__ передавати
# first name
# last name
# email
# tech_stack
# main_skill
# main_skill_grade
# Створити @property метод який повертає first name + ‘ ‘ + last name
# Створити @classmethod generate_candidates, який приймає в якості аргументу шлях до файлу
# Метод generate_candidates має повертати список об’єктів класу Candidate
# Файл тут https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv

import csv


class Candidate:
    def __init__(self, fname, lname, email, tech_stack, main_skill, main_skill_grade) -> None:
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __repr__(self) -> str:
        return f'{self.full_name} | {self.email} | {self.tech_stack} | {self.main_skill} | {self.main_skill_grade}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(self, path):
        candidate_list = []

        try:
            with open(path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for item in reader:
                    fname, lname = item[0].split()
                    email = item[1]
                    ts = item[2].split('|')
                    ms = item[3]
                    msg = item[4]
                    candidate_list.append(Candidate(fname, lname, email, ts, ms, msg))
        except:
            pass

        return candidate_list


def main():
    print(*Candidate.generate_candidates('candidates.csv'), sep='\n')

if __name__ == "__main__":
    main()