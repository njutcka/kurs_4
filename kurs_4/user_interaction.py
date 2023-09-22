from vacancy import Vacancy
from vacancy_file_manager import JSONSaver
from api import HeadHunterAPI, SuperJobAPI
from pprint import pprint
def user_interaction():

    print("Введите ключевое слово для поиска")
    search_query = input()

    print("Выберите сайт для поиска вакансий:\n"
                               "1. HH\n"
                               "2. SJ\n"
                               "3. HH и SJ\n")
    site_selection = int(input())
    while True:

        if site_selection == 1:
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.get_vacancies(search_query)
            all_vacancies = hh_api.get_formated_vacancies(hh_vacancies)
            js_saver = JSONSaver(search_query)
            js_saver.save_vacancies(all_vacancies)
            break

        elif site_selection == 2:
            sj_api = SuperJobAPI()
            sj_vacancies = sj_api.get_vacancies(search_query)
            all_vacancies = sj_api.get_formated_vacancies(sj_vacancies)
            js_saver = JSONSaver(search_query)
            js_saver.save_vacancies(all_vacancies)
            break

        elif site_selection == 3:
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.get_vacancies(search_query)
            hh_formated_vacancies = hh_api.get_formated_vacancies(hh_vacancies)
            sj_api = SuperJobAPI()
            sj_vacancies = sj_api.get_vacancies(search_query)
            sj_formated_vacancies = sj_api.get_formated_vacancies(sj_vacancies)
            all_vacancies = hh_formated_vacancies + sj_formated_vacancies
            js_saver = JSONSaver(search_query)
            js_saver.save_vacancies(all_vacancies)
            break

        else:
            print("Выберите 1, 2 или 3.")


    vacancies = js_saver.select_vacancies()

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    sorted_vacancies = Vacancy.sorted_vacancies(vacancies)
    Vacancy.top_vacancies(sorted_vacancies, top_n)

    filter_word = input('Введите город для вакансий: ')
    filter_word.lower()
    filter_vacancies = Vacancy.filtered_vacancies(vacancies, filter_word)

    if not filter_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")


    print("Продолжить работу?\n"
          "1. да\n"
          "2. нет\n")
    off = int(input())
    if off == 2:
        js_saver.delete_vacancy()


