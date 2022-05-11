documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(document_list, shelves):
    number = input('Введите номер документа: ')
    for document in document_list:
        if number in document.values():
            print(f'Владелец документа №{number} - {document["name"]}')
            return
    print('Такого документа не существует')


def get_shelf(document_list, shelves):
    number = input('Введите номер документа: ')
    for key, value in shelves.items():
        if number in value:
            print(f'Документ №{number} находится на полке {key} ')
            return
    print('Документ отсутствует на полке')


def list_show(document_list, shelves):
    for document in document_list:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def add_doc(document_list, shelves):
    document_type = input('Введите тип документа: ')
    document_number = input('Введите номер документа: ')
    document_owner = input('Введите имя владельца документа: ')
    shelf = input('На какой полке будет храниться документ: ')
    if shelf in shelves.keys():
        document = {'type': document_type, 'number': document_number, 'name': document_owner}
        document_list.append(document)
        shelves[shelf].append(document_number)
        print('Документ был добавлен в каталог и на полку')
        return
    print('Документ не может быть добавлен в каталог и на полку. Такой полки не существует')


def del_document(document_list, shelves):
    document_number = input('Введите номер документа для удаления: ')
    deleted = False
    for doc in document_list:
        if document_number == doc['number']:
            document_list.remove(doc)
            print(f'Документ №{document_number} удален из каталога')
            delete = True
    for key, value in shelves.items():
        if document_number in value:
            value.remove(document_number)
            print(f'Документ №{document_number} удален с полки')
            deleted = True
    if not deleted:
        print('Такого документа не существует')


def move(document_list, shelves):
    last_shelves = input('Введиет номер целевой полки: ')
    if last_shelves not in shelves.keys():
        print('Такой полки нет, введите команду заново и укажите существующую полку')
        return
    document_number = input('Введите номер документа, который надо переместить')
    for key, value in shelves.items():
        if document_number in value:
            value.remove(document_number)
            shelves[last_shelves].append(document_number)
            print(f'Документ №{document_number} перемещен на полку{last_shelves}')
            return
    print('Такого документа не существует')


def add_shelf(document_list, shelves):
    new_shelf = input('Введите номер новой полки для добавления: ')
    if new_shelf not in shelves.keys():
        shelves[new_shelf] = []
        print(f'Полка{new_shelf}добавлена')
        return
    print('Такая полка уже есть')


dict_commands = {
    'p': get_name,
    's': get_shelf,
    'l': list_show,
    'a': add_doc,
    'd': del_document,
    'm': move,
    'as': add_shelf
}


def run():
    general_help = """Введите команду:
    p - узнать имя человека по номеру документа;
    s - узнать номер полки по номеру документа;
    l - вывести список паспортов и имен;
    a - добавить новый документ;
    d - удалить документ по номеру;
    m - переместить документ;
    as - добавить новую полку;
    q - выход."""
    print(general_help)

    while True:
        command = input('\nВведите команду: ')
        if command in dict_commands.keys():
            dict_commands[command](documents, directories)
        elif command == 'q':
            print('Выход из программы')
            break
        else:
            print('Такой команды не существует')


run()





