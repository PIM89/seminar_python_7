# Вывод данных
def view_data(data):
    print(data)

# Ввод данных абонента
def input_data():
    surname = (input('Введите фамилию: ')).capitalize()
    name = (input('Введите имя: ')).capitalize()
    patronymic = (input('Введите отчество: ')).capitalize()
    while True:
        phone = input('Введите номер телефона(формат 79254452356): ')
        try:
            phone = int(phone)
            break
        except:
            view_data('Введенные данные не являются телефонным номером!')
    data = {'Фамилия': surname, 'Имя': name, 'Отчество': patronymic, 'Телефон': str(phone)}
    return data