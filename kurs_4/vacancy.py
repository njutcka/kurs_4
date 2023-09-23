class Vacancy:

    all_vacancy = []
    def __init__(self, name, salary, city, url, currency, currency_value, api):
        self.name = name
        if salary is None:
            self.salary = 0
        else:
            self.salary = salary
        self.city = city
        self.url = url
        self.currency = currency
        if currency_value is None:
            self.currency_value = 0
        else:
            self.currency_value = currency_value
        self.api = api
        self.converted_salary = self.salary * self.currency_value

    def __lt__(self, other):
        return self.converted_salary < other.converted_salary

    def __str__(self):
        return self.city

    def __repr__(self):
        return f"{self.api}: Вакансия {self.name} с зп {self.salary}руб, в городе {self.city}, ссылка {self.url} "

    def __dict__(self):
        return {"name": self.name,
                "salary": self.salary,
                "currency": self.currency,
                "city": self.city,
                "url": self.url}


    @staticmethod
    def filtered_vacancies(vacancies,filter_word):
        filtered_vacancies = []
        for vacancy in vacancies:
            v = vacancy.__str__()
            if v.lower() == filter_word.lower():
                filtered_vacancies.append(vacancy)
                print(vacancy.__repr__())
            else:
                continue
        return filtered_vacancies


    @staticmethod
    def sorted_vacancies(vacancies):
        sorted_vacansies = sorted(vacancies, reverse=True)
        return sorted_vacansies


    @staticmethod
    def top_vacancies(sorted_vacansies, top_n):
        for vacancy in sorted_vacansies[:top_n]:
            print(vacancy.__repr__())


