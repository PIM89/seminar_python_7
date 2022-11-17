import view
import operation
import log

def button_click():
    select = ''
    while select != '5':
        select = input('Выбор режима работы с телефонным справочником...\n'\
            'Для импорта контакта укажите: 1\n'\
            'Для экспорта контактов в необходимом формате укажите: 2\n'\
            'Для поиска контакта укажите: 3\n'\
            'Для чтения справочника укажите: 4\n'\
            'Для завершения работы программы укажите: 5\n\n'\
            'Выбранный режим: ')
        if select == '1':
            result = view.input_data()
            operation.record_data(result)
            log.write(select, result)
        if select == '2':
            operation.exp()
            log.write(select)
        if select == '3':
            search = (input('Укажите фамилию или имя абонента для поиска: ')).capitalize()
            operation.search_subscriber(search)
            log.write(select, search)
        if select == '4':
            operation.reading_reference()
            log.write(select)
        if select == '5':
            log.write(select)