import csv
import os.path
import view

# Запись данных
def record_data(dictt):
    file_exists = os.path.isfile('reference.csv')
    with open('reference.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
        writer = csv.DictWriter(f, delimiter = ';', fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(dictt)
    view.view_data('Данные записаны успешно.\n')

# Чтение всего справочника
def reading_reference():
    try:
        with open('reference.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                view.view_data('Фамилия: {}, Имя: {}, Отчество: {}, Телефон: {}'.format(row['Фамилия'], row['Имя'], row['Отчество'], row['Телефон']))
    except:
        view.view_data('Телефонный справочник отсутствует!\n')


# Поиск абонента
def search_subscriber(strr):
    try:
        with open('reference.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            flag = False
            for row in reader:
                if strr in row.values():
                    view.view_data('Результат поиска:\n {}\n'.format(row))
                    flag = True
            if flag == False:
                view.view_data('Такого абонента в справочнике нет.')
    except:
        view.view_data('Телефонный справочник отсутствует!\n')


# Экспорт справочника в разных форматах
def exp():
    output = {'1': 'Фамилия', '2': 'Имя', '3': 'Отчество', '4': 'Телефон'}
    try:
        output_user = (input('Введите формат вывода справочника (цифры через запятую)...\n'\
                        '1 - "Фамилия", 2 - "Имя", 3 - "Отчество", 4 - "Номер телефона"\n'\
                        'например: 1,4 => Фамилия: Иванов Телефон: 89998887744\n')).replace(' ', '').split(',')

        with open('reference.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            rez = ''
            for row in reader:
                for elem in output_user:
                    rez += '{}: {} \n'.format(output[elem], row[output[elem]])
            view.view_data(rez)
    except:
        view.view_data('Телефонный справочник отсутствует!\n')