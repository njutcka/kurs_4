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
                               "3. HH и SJ")
    site_selection = input()
    #создаем json файл с массивом вакансий по ключевому слову
    #цикл работет нормально если ввести 1 2 или 3, а если другое значение то по идее он должен снова спрашивать,
    #а мне начинает выдавать бесконечно строку "Выберите 1, 2 или 3."
    while True:

        if site_selection == '1':
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.get_vacancies(search_query)
            all_vacancies = hh_api.get_formatted_vacancies(hh_vacancies)
            js_saver = JSONSaver(search_query)
            js_saver.save_vacancies(all_vacancies)
            break

        elif site_selection == '2':
            sj_api = SuperJobAPI()
            sj_vacancies = sj_api.get_vacancies(search_query)
            all_vacancies = sj_api.get_formatted_vacancies(sj_vacancies)
            js_saver = JSONSaver(search_query)
            js_saver.save_vacancies(all_vacancies)
            break

        elif site_selection == '3':
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.get_vacancies(search_query)
            hh_formatted_vacancies = hh_api.get_formatted_vacancies(hh_vacancies)
            sj_api = SuperJobAPI()
            sj_vacancies = sj_api.get_vacancies(search_query)
            sj_formatted_vacancies = sj_api.get_formatted_vacancies(sj_vacancies)
            all_vacancies = hh_formatted_vacancies + sj_formatted_vacancies
            js_saver = JSONSaver(search_query)
            js_saver.save_vacancies(all_vacancies)
            break

        else:
            print("Выберите 1, 2 или 3.")

    #создаем экземпляры класса Vacancy по данным из файла
    vacancies = js_saver.select_vacancies()

    while True:
        print('Показать вакансии?\n'
              '1. да\n'
              '2. нет')
        show = input('')
        if show == '1':
            while True:
                print('1. Вывести топ вакансий по зарплате.\n'
                      '2. Список вакансий по выбранному городу.\n'
                      '3. Список вакансий по желаемой зарплате.')
                how_show = input()
                if how_show == '1':
                    # ввыводит топ вакансий по зарплате
                    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                    sorted_vacancies = Vacancy.sorted_vacancies(vacancies)
                    Vacancy.top_vacancies(sorted_vacancies, top_n)
                    break
                elif how_show == '2':
                    # фильтрация по названию города
                    filter_word = input('Введите город для вакансий: ')
                    filter_vacancies = Vacancy.filtered_vacancies(vacancies, filter_word)
                    if not filter_vacancies:
                        print("Нет вакансий, соответствующих заданным критериям.")
                    break
                elif how_show == '3':
                    min_salary = int(input("Минимальная зарплата = "))
                    print(js_saver.get_vacancies_by_salary(min_salary))
                    break
                else:
                    print('Выберите 1, 2 или 3.')

        elif show == '2':
            while True:
                print('Закончить работу с этим ключевым словом?\n'
                      '1. да\n'
                      '2. нет')
                done = input()
                if done == '1':
                    js_saver.delete_vacancy()
                    return
                elif done == '2':
                    break
                else:
                    print('Выберите 1 или 2.')
