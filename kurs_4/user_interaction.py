from vacancy import Vacancy
from vacancy_file_manager import JSONSaver
from api import HeadHunterAPI, SuperJobAPI

def user_interaction():
    """Функция для взаимодействия с пользователем"""
    print("Введите ключевое слово для поиска")
    search_query = input()
    print("Выберите сайт для поиска вакансий:\n"
          "1. HH\n"
          "2. SJ\n"
          "3. HH и SJ")
    #создаем json файл с массивом вакансий по ключевому слову
    #пользоваетль выбирает с какого сайта будут вакансии с одного или сразу с обоих
    while True:
        site_selection = input()
        api_list = []
        all_vacancies = []
        if site_selection in ('1', '3'):
            hh_api = HeadHunterAPI()
            api_list.append(hh_api)
        if site_selection in ('2', '3'):
            sj_api = SuperJobAPI()
            api_list.append(sj_api)
        if site_selection not in ('1', '2', '3'):
            print('Выберите 1, 2 или 3')
            continue

        for api in api_list:
            api_vacancies = api.get_vacancies(search_query)
        all_vacancies.extend(api.get_formatted_vacancies(api_vacancies))
        js_saver = JSONSaver(search_query)
        js_saver.save_vacancies(all_vacancies)
        break

    #создаем экземпляры класса Vacancy по данным из файла
    vacancies = js_saver.select_vacancies()

    #Цикл для вывода вакансий, на выбор топ по зарплате, фильтр по городу или список от мин зарплаты
    while True:
        print('Показать вакансии?\n'
              '1. да\n'
              '2. нет')
        show = input('')
        if show == '1':
            print('1. Вывести топ вакансий по зарплате.\n'
                  '2. Список вакансий по выбранному городу.\n'
                  '3. Список вакансий по желаемой зарплате.')

            while True:
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
                    js_saver.get_vacancies_by_salary(min_salary)
                    break
                else:
                    print('Выберите 1, 2 или 3.')

        #ветка для окончания программы и удаления файла с вакансиями
        elif show == '2':
            print('Сохранить файл с вакансиями?\n'
                  '1. да\n'
                  '2. нет')
            while True:
                done = input()
                if done == '1':
                    break
                elif done == '2':
                    js_saver.delete_vacancy()
                    break
                else:
                    print('Выберите 1 или 2.')
            return
