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
    #создаем json файл с массивом вакансий по ключевому слову
    #цикл работет нормально если ввести 1 2 или 3, а если другое значение то по идее он должен снова спрашивать,
    #а мне начинает выдавать бесконечно строку "Выберите 1, 2 или 3."
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

#создаем вакансии по даным считанным из файла
    vacancies = js_saver.select_vacancies()
#ввыводит топ вакансий по зарплате
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    sorted_vacancies = Vacancy.sorted_vacancies(vacancies)
    Vacancy.top_vacancies(sorted_vacancies, top_n)
#фильтрация по названию города
    filter_word = input('Введите город для вакансий: ')
    filter_word.lower()
    filter_vacancies = Vacancy.filtered_vacancies(vacancies, filter_word)

    if not filter_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")

#я решила сделать в vacancy_file_manager ф-ию удаляющую файл с вакансиями,
#чтобы не замусоривать папку, но пока не продумала логику
    print("Продолжить работу?\n"
          "1. да\n"
          "2. нет\n")
    off = int(input())
    if off == 2:
        js_saver.delete_vacancies()


