import json
import os
from kurs_4.vacancy import Vacancy
from abc import ABC, abstractmethod

class Saver(ABC):
    """Абстрактный класс, для сохранения данных о вакансиях в файл"""
    @abstractmethod
    def save_vacancies(self):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(Saver):
    """Класс, для сохранения данных о вакансиях в json файл"""
    def __init__(self, key_word):
        """Метод инициализации экземпляра класса с полем имя файла
        принимает: ключевое слово для поиска вакансий запрощенное от пользователя"""
        self.file_name = f'{key_word.title()}.json'

    def save_vacancies(self, vacancies):
        """Метод записи вакансий в файл"""
        with open(self.file_name, "w", encoding="utf-8") as json_file:
            json.dump(vacancies, json_file, ensure_ascii=False, indent=2)

    def select_vacancies(self):
        """Метод для создания списка экземпляров класса Vacancy по данным из файла
        возвращает: список вакансий"""
        with open(self.file_name, "r", encoding="utf-8") as json_file:
            vacancies = json.load(json_file)
        vacancies = [Vacancy(**v) for v in vacancies]
        return vacancies

    def get_vacancies_by_salary(self, min_salary):
        """Метод выводит список вакансий из файла, выбирая по зарплате
        принимает: минимальную зарплату (от пользователя)"""
        with open(self.file_name, "r", encoding="utf-8") as json_file:
            vacancies = json.load(json_file)
        for v in vacancies:
            if not v['salary'] == None:
                if not v['currency_value'] == None:
                    if int(v['salary'])*float(v['currency_value']) >= min_salary:
                        vacancy = Vacancy(**v)
                        print(vacancy.__repr__())
                continue
            continue

    def delete_vacancy(self):
        """Метод удаляет файл с данными"""
        os.remove(self.file_name)
