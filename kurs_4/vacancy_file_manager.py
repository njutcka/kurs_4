import json
import os
from kurs_4.vacancy import Vacancy
from abc import ABC, abstractmethod

# Сохранение информации о вакансиях в файл
class Saver(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(Saver):
    def __init__(self, key_word):
        self.file_name = f'{key_word.title()}.json'

    def save_vacancies(self, vacancies):
        with open(self.file_name, "w", encoding="utf-8") as json_file:
            json.dump(vacancies, json_file, ensure_ascii=False, indent=2)

    def select_vacancies(self):
        with open(self.file_name, "r", encoding="utf-8") as json_file:
            vacancies = json.load(json_file)
        vacancies = [Vacancy(**v) for v in vacancies]
        return vacancies

    @staticmethod
    def add_vacancy(vacancy):
        with open("vacansies.json", "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
        content.append(vacancy.__dict__())
        with open("vacansies.json", "w", encoding="utf-8") as json_file:
            json.dump(content.append(vacancy.__dict__()), json_file, ensure_ascii=False, indent=2)

    def get_vacancies_by_salary(self):
        pass

    def delete_vacancy(self):
        os.remove(self.file_name)

