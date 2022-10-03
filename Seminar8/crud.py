import csv
import json
import os.path
import sqlite3
import pandas as pd


db_file_name = ''
db = []
global_id = 0  # id для добавления пользователей


def init_data_base(file_name='company_base.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(last_name='', first_name='', position='', number='', salary=''):
    global global_id
    global db
    global db_file_name
    if(last_name == ''):
        print("ALARM NO LAST_NAME SPECIFIED!!!!!1111")
        return
    if(first_name == ''):
        print("ALARM NO SURNAME SPECIFIED!!!!!1111")
        return
    if(position == ''):
        print("ALARM NO POSITION SPECIFIED!!!!!1111")
        return
    if(number == ''):
        print("ALARM NO TELEPHONE NUMBER SPECIFIED!!!!!1111")
        return
    if(salary == ''):
        print("ALARM NO SALARY SPECIFIED!!!!!1111")
        return

    for row in db:
        if(row[1] == last_name.title() and row[2] == first_name.title() \
            and row[3] == position and row[4] == number \
                and row[5] == salary):
            print("already exist")
            return

    global_id += 1
    new_row = [str(global_id), last_name.title(), first_name.title(), \
        position, number, salary]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


# поиск (если нужно выгрузить все: result = retrive())
def retrive(id='', last_name='', position='', number='', salary=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(last_name != '' and row[1] != last_name.title()):
            continue
        if(position != '' and row[3] != position):
            continue
        if(number != '' and row[4] != number):
            continue
        if(salary != '' and row[5] != salary):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Сотрудники не найдены'
    else:
        # выход список списков (переделать в строку с разделителем)
        return result


def update(id='', new_last_name='', new_first_name='', new_position='', new_number='', new_salary=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for update')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_last_name != ''):
                    row[1] = new_last_name.title()

                if(new_first_name != ''):
                    row[2] = new_first_name.title()

                if(new_position != ''):
                    row[3] = new_position

                if(new_number != ''):
                    row[4] = new_number

                if(new_salary != ''):
                    row[5] = new_salary

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


def create_json():
    csvfile = open('company_base.csv', 'r')
    jsonfile = open('file.json', 'w')

    fieldnames = ('id','last_name','first_name','position','number','salary')
    reader = csv.DictReader( csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')
        

def create_cmv():
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()
    users = pd.read_csv('company_base.csv')
    users.to_sql('users', conn, if_exists='append', index = False, chunksize = 10000)


def get_token():
    file = open('token.csv', 'r')
    for i in file:
        token = i
    file.close()
    return token
