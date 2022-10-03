import crud as cr
import logger as lg


print('\nБаза сотрудников компании')


def show_menu() -> int:
    while True:
        print("\n" + "=" * 20)
        print("Выберите необходимое действие")
        print('1. Найти сотрудника')
        print('2. Сделать выборку сотрудников по должности')
        print('3. Сделать выборку сотрудников по зарплате')
        print('4. Добавить сотрудника')
        print('5. Удалить сотрудника')
        print('6. Обновить данные сотрудника')
        print('7. Экспортировать данные в формате json')
        print('8. Экспортировать данные в формате cmv')
        print("9. Закончить работу \n")
        n = сhecking_the_number(input('Введите номер необходимого действия: \n'))

        if n == 1:
            lg.logging.info('The user has selected item number 3')
            search = input('Введите фамилию: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(last_name=search))

        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            search = input('Введите должность: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(position=search))

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            search = input('Введите зарплату в рублях: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(salary=search))

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            last_name = input('Введите фамилию: ')
            lg.logging.info('User entered: {last_name}')
            first_name = input('Введите имя: ')
            lg.logging.info('User entered: {first_name}')
            position = input('Введите должность: ')
            lg.logging.info('User entered: {position}')
            number = input('Введите номер телефона: ')
            lg.logging.info('User entered: {number}')
            salary = input('Введите зарплату в рублях: ')
            lg.logging.info('User entered: {salary}')
            cr.create(last_name, first_name, position, number, salary)

        elif n == 5:
            lg.logging.info('The user has selected item number 5')
            print('1. Найти сотрудника по должности')
            print('2. Найти сотрудника по фамилии')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 5.1')
                search = input('Введите должность: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(position=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 5.2')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(last_name=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
        
        elif n == 6:
            lg.logging.info('The user has selected item number 6')
            print('1. Обновить должность сотрудника')
            print('2. Обновить фамилию сотрудника')
            print('3. Обновить зарплату сотрудника')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                lg.logging.info('The user has selected item number 6.1')
                search = input('Введите должность: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(position=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_position = input('Введите новую должность: ')
                lg.logging.info('User entered: {new_position}')
                cr.update(id=user_id, new_position=new_position)

            elif change == 2:
                lg.logging.info('The user has selected item number 6.2')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(last_name=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_last_name = input('Введите новую фамилию: ')
                lg.logging.info('User entered: {new_last_name}')
                cr.update(id=user_id, new_last_name=new_last_name)

            elif change == 3:
                lg.logging.info('The user has selected item number 6.3')
                search = input('Введите зарплату: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(salary=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_salary = input('Введите новую зарплату: ')
                lg.logging.info('User entered: {new_salary}')
                cr.update(id=user_id, new_salary=new_salary)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 7:
            lg.logging.info('The user has selected item number 7')
            lg.logging.info('User entered: {search}')
            print(cr.create_json())

        elif n == 8:
            lg.logging.info('The user has selected item number 7')
            lg.logging.info('User entered: {search}')
            print(cr.create_cmv())

        elif n == 9:
            lg.logging.info('End')
            print('Спасибо за работу!')
            break

        else:
            lg.logging.info('User entered an invalid menu value: {n}')
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

# def find(user_choice(n)):
# делаем срез по таблице и выдаем необходимые данные.


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('User entered an invalid menu value: {arg}')
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)
    