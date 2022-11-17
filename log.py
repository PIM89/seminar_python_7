from datetime import datetime

def write(oper, data = None):
    operation = {'1': '"Импорт контакта"', '2': '"Экспорт контактов в необходимом формате"', '3': '"Поиск контакта"', '4': '"Чтение справочника"', '5': '"Выход из приложения"'}
    with open('log_cash.txt', 'a', encoding='utf-8') as l:
        if oper == '1':
            result = 'Выполняемая операция - {}. Информация - {}. Время выполнения - {}'.format(operation[oper], data, datetime.now())
        else: result = 'Выполняемая операция - {}. Время выполнения - {}'.format(operation[oper], datetime.now())
        l.write(f'{result}' + '\n')