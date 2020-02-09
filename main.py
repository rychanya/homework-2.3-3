documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "10006", "name": "Аристашка Павлов"},
    {"type": "insurance", "number": "10007"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765', '2'],
        '2': ['10006', '5400 028765', '5455 002299', '2'],
        '3': []
      }

def add_shelf(shelf_name):
    if shelf_name in directories.keys():
        print('Такая полка уже есть.')
    else:
        directories[shelf_name] = []
        print('Полка добавлена')

def get_owner_name_by_doc_number(number: str):
    res = [document.get('name') for document in documents if document.get('number') == number]
    if len(res) == 0:
        print(f'Документа с номером {number} не найден')
    elif len(res) == 1:
        print(f'Документ с номером {number} принадлежит {res[0]}')
    else:
        print(f'Документ с номером {number} не унекален. Возможные владельцы:')
        print(res)

def get_shelf_number_by_doc_number(doc_number):
    shelfs = [shelf_number for shelf_number, docs in directories.items() if doc_number in docs]
    if len(shelfs) == 0:
        print(f'Документа с номером {doc_number} нет на полках')
    elif len(shelfs) == 1:
        print(f'Документ с номером {doc_number} находиться на полек номер {shelfs[0]}')
    else:
        print('В записях ошибка!')
        print(f'Документ с номером {doc_number} находиться на одной из полок:')
        print(shelfs)

def print_list():
    print('Список всех документов:')
    for doc in documents:
        doc_type = doc.get("type")
        doc_number = doc.get("number")
        doc_owner = doc.get("name")
        print(f'{doc_type} "{doc_number}" "{doc_owner}"')

def add_doc_to_shelf():
    doc_number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    doc_owner = input('введите владельца: ')
    shelf_number = input('Введите номер полки: ')
    doc = {
        'type': doc_type,
        'number': doc_number,
        'name': doc_owner
    }
    if shelf_number not in directories:
        print(f'Полки с номром {shelf_number} нет в базе. Если вы хотите ее добавить введите ее номер еще раз.')
        if shelf_number != input():
            print('Полка не добавлена. Данные не сохранены')
            return
    documents.append(doc)
    directories.setdefault(shelf_number, []).append(doc_number)
    print('Документ добавлен.')

def delete_by_doc_number_and_return_new_list(doc_number):
    for name in directories.keys():
        while True:
            try:
                directories[name].remove(doc_number)
            except ValueError:
                break
    return [doc for doc in documents if doc.get('number') != doc_number]

def move_to_shelf(doc_number, new_shelf):
    if new_shelf not in directories.keys():
        print(f'Полка с номером {new_shelf} не существует. Сначала добавьте новую полку командой "as".')
        return
    if any([(doc_number in docs) for docs in directories.values()]):
        delete_by_doc_number_and_return_new_list(doc_number)
        directories[new_shelf].append(doc_number)
        print(f'Документ с номером {doc_number} перемещен на полку {new_shelf}.')
    else:
        print('Документа нет на полках. Сначала добавьте документ командой "a".')

def print_all_doc_name():
    for doc in documents:
        try:
            print(f'{doc["name"]} - владелец документа {doc.get("number")}')
        except KeyError:
            print(f'У документа {doc.get("number")} нет владельца')

if __name__ == '__main__':
    print('''
p  – people    – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
l  – list      – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
s  – shelf     – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
a  – add       – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, 
                 на котором он будет храниться;
d  – delete    – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
m  – move      – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
pa – print all – команда, которая выведит список всех владельцов документов;
q  – quite     – Выход.
             ''')
    while True:
        comand = input('Введите команду: ')
        if comand == 'q':
            break
        elif comand == 'p':
            get_owner_name_by_doc_number(input('Введите номер документа: '))
        elif comand == 'l':
            print_list()
        elif comand == 's':
            get_shelf_number_by_doc_number(input('Введите номер документа: '))
        elif comand == 'a':
            add_doc_to_shelf()
        elif comand == 'as':
            add_shelf(input('Введите номер новой полки: '))
        elif comand == 'd':
            documents = delete_by_doc_number_and_return_new_list(input('Введите номер документа: '))
        elif comand == 'm':
            move_to_shelf(input('ведите номер документа: '), input('На какую полку переместить? '))
        elif comand == 'pa':
            print_all_doc_name()
        else:
            print('Такой команды нет. Попробуйте еще.')
