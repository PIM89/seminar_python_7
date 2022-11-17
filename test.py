import view
import csv


# # # # # def search_subscriber(strr):
# # # # #     with open('reference.txt', 'r', encoding='utf-8') as f:
# # # # #         data = f.readlines()
# # # # #         flag = False
# # # # #         for elem in data:
# # # # #             if strr in elem:
# # # # #                 view.view_data(elem)
# # # # #                 flag = True
# # # # #         if flag == False: print('Такого абонента в справочнике нет!')

# # # # # # search_subscriber('12')

# # # # # def reading_reference():
# # # # #     with open('reference.txt', 'r', encoding='utf-8') as f:
# # # # #         data = ''.join(f.readlines())
# # # # #         view.view_data(data)

# # # # # reading_reference()

# # # # # print('Выбор режима работы...\n'\
# # # # #         'Для импорта контакта напишите: 1\n'\
# # # # #         'Для экспорта контакта напишите: 2')

# # # # def search_subscriber(strr):
# # # #     with open('reference.txt', 'r', encoding='utf-8') as f:
# # # #         data = f.readlines()
# # # #         flag = False
# # # #         for elem in data:
# # # #             if strr in elem:
# # # #                 view.view_data(elem)
# # # #                 flag = True
# # # #         if flag == False: print('Такого абонента в справочнике нет.')

# # # def input_phone():
# # #     while True:
# # #         some_str = input('Введите номер телефона(формат 79254452356): ')
# # #         try:
# # #             some_str = int(some_str)
# # #             break
# # #         except:
# # #             print('Введенные данные не являются телефонным номером!')
# # #     return some_str


# # # print(input_phone())


# # def input_data():
# #     surname = input('Введите фамилию: ')
# #     name = input('Введите имя: ')
# #     while True:
# #         phone = input('Введите номер телефона(формат 79254452356): ')
# #         try:
# #             phone = int(phone)
# #             break
# #         except:
# #             print('Введенные данные не являются телефонным номером!')
# #     return surname, name, str(phone)

# # print(type(input_data()))

# def input_data():
#     surname = input('Введите фамилию: ')
#     name = input('Введите имя: ')
#     while True:
#         phone = input('Введите номер телефона(формат 79254452356): ')
#         try:
#             phone = int(phone)
#             break
#         except:
#             view_data('Введенные данные не являются телефонным номером!')
#     data = {'Surname': surname, 'Name': name, 'Phone': str(phone)}
#     return data

# print(input_data())

# # Ввод данных
# # def input_surname():
# #     some_str = input('Введите фамилию: ')
# #     return some_str

# # def input_name():
# #     some_str = input('Введите имя: ')
# #     return some_str

# # def input_phone():
# #     while True:
# #         some_str = input('Введите номер телефона(формат 79254452356): ')
# #         try:
# #             some_str = int(some_str)
# #             break
# #         except:
# #             print('Введенные данные не являются телефонным номером!')
# # #     return some_str



# def search_subscriber(strr):
#     try:
#         with open('reference.csv', 'r', encoding='utf-8') as f:
#             reader = csv.DictReader(f)
#             flag = False
#             for row in reader:
#                 if strr in row:
#                     view.view_data(row)
#                     flag = True
#             if flag == False: print('Такого абонента в справочнике нет.')
#     except:
#         print('Телефонный справочник отсутствует!\n')


# сначала запишем файл 'names.csv', который 
# # потом прочитаем как список словарей
# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# # 13
# # 13
# # 16

# # читаем CSV файл как список словарей, ключи 
# # которого заданы первой строкой файла 'names.csv'
# with open('names.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(type(row))

# Eric Idle
# John Cleese
# print(row)
# {'first_name': 'John', 'last_name': 'Cleese'}

d = {'first_name': 'Baked', 'last_name': 'Beans'}
p = input('давай: ')
if p in d.values():
    print(d['first_name'])