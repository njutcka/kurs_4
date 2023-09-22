from abc import ABC, abstractmethod
import json
import requests
from pprint import pprint

# Создание экземпляра класса для работы с API сайтов с вакансиями
class API(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass

class HeadHunterAPI(API):
    def get_vacancies(self, search_query):
        params = {
            "text": search_query,
            "per_page": 100
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        vacancies = response.json()['items']
        return vacancies

    def get_formated_vacancies(self, vacancies):
        formated_vacancies = []
        with open('../currency.json') as file:
            currencies = json.load(file)
        for vacancy in vacancies:
            salary = vacancy['salary']['from'] if vacancy['salary'] else None
            currency = vacancy['salary']['currency'] if vacancy['salary'] else None
            formated_vacancies.append({
                'name': vacancy['name'],
                'salary': salary,
                'currency': currency,
                'currency_value': currencies.get(currency),
                'city': vacancy['area']['name'],
                'url': vacancy['alternate_url'],
                'api': 'HH'
            })
        return formated_vacancies

class SuperJobAPI(API):
    def get_vacancies(self, search_query):
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

    def get_formated_vacancies(self, vacancies):
        formated_vacancies = []
        for vacancy in vacancies:
            salary = vacancy['payment_from'] if vacancy['payment_from'] else None
            currency = vacancy['currency'] if vacancy['currency'] else None
            formated_vacancies.append({
                'name': vacancy['profession'],
                'salary': salary,
                'currency': currency,
                'currency_value': 1,
                'city': vacancy['town']['title'],
                'url': vacancy['link'],
                'api': 'SJ'
            })
        return formated_vacancies
