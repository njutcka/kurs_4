from user_interaction import user_interaction

if __name__ == "__main__":

    user_interaction()
    print('Повторить поиск? \n'
          '1. да\n'
          '2. нет')
    while True:
        flag = input()
        if flag == '1':
            user_interaction()
        elif flag == '2':
            break
        else:
            print('Выберите 1 или 2.')
            continue
