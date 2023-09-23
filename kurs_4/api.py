from abc import ABC, abstractmethod
import json
import requests
from pprint import pprint

class API(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""
    @abstractmethod
    def get_vacancies(self, search_query):
        pass

class HeadHunterAPI(API):
    """Класс для работы с api сайта HeadHanter"""
    def get_vacancies(self, search_query):
        """Получает с сайта список из первых 100 вакансий
        принимает: ключевое слово
        возвращвет: список"""
        params = {
            "text": search_query,
            "per_page": 100
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        vacancies = response.json()['items']
        return vacancies

    def get_formatted_vacancies(self, vacancies):
        """Приводит вакансии к стандартному виду
        принимает: список вакансий
        возвращает: отформатированный список вакансий"""
        formatted_vacancies = []
        with open('../currency.json') as file:
            currencies = json.load(file)
        for vacancy in vacancies:
            salary = vacancy['salary']['from'] if vacancy['salary'] else None
            currency = vacancy['salary']['currency'] if vacancy['salary'] else None
            formatted_vacancies.append({
                'name': vacancy['name'],
                'salary': salary,
                'currency': currency,
                'currency_value': currencies.get(currency),
                'city': vacancy['area']['name'],
                'url': vacancy['alternate_url'],
                'api': 'HH'
            })
        return formatted_vacancies

class SuperJobAPI(API):
    """Класс для работы с api сайта SuperJob"""
    def get_vacancies(self, search_query):
        """Получает с сайта список из первых 100 вакансий
                принимает: ключевое слово
                возвращвет: список"""
        headers = {
            'X-Api-App-Id': 'v3.r.137832039.131046b8364dfa6a6a3351df7b2e9cb4b9277f47.78a0807c6f0e0d78ba965412fef552960f49ab39'
        }
        params = {
            "keyword": search_query,
            "count": 100
        }
        response = requests.get('https://api.superjob.ru/2.0/vacancies', headers=headers, params=params)
        vacancies = response.json()['objects']
        return vacancies

    def get_formatted_vacancies(self, vacancies):
        """Приводит вакансии к стандартному виду
        принимает: список вакансий
        возвращает: отформатированный список вакансий"""
        formatted_vacancies = []
        for vacancy in vacancies:
            salary = vacancy['payment_from'] if vacancy['payment_from'] else None
            currency = vacancy['currency'] if vacancy['currency'] else None
            formatted_vacancies.append({
                'name': vacancy['profession'],
                'salary': salary,
                'currency': currency,
                'currency_value': 1,
                'city': vacancy['town']['title'],
                'url': vacancy['link'],
                'api': 'SJ'
            })
        return formatted_vacancies
