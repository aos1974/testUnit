# Список документов

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "10007", "name": "Петр Сидоров"},
        {"type": "order", "number": "12-06", "name": "Иван Сидоров"}
      ]

# Список полок

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '10007'],
    '3': ['12-06']
    }

# Поиск человека по номеру документа
def find_people(fnumber):
    
    fname = ''

    for d in documents:
        if fnumber in d.values():
            fname = d.get('name')

    return(fname)

# Поиск расположения документа
def find_dir(fnumber):
    
    fdir = ''

    for d in directories:
        if fnumber in directories.get(d):
            fdir = d

    return(fdir)

# Удаление документа

def del_document(number):

    # удаляем документ "с полки"
    i = find_dir(number)
    directories[i].remove(number)

    # удаляем документ из списка
    for i, d in enumerate(documents):
        if number in d.values():
            del(documents[i])

    return()

# Перемещение документа

def mov_document(number, dir):

    # удаляем документ со старой "полки"
    i = find_dir(number)
    directories[i].remove(number)

    # записываем документ на новую "полку"
    directories[dir].append(number)

    return()


#
# Основная программа
#

HELP_STRING = ("""
    p - поиск человека по номеру документа
    s - поиск расположения документа 
    l - вывод списка всех хранящихся документов
    a - добавление нового документа
    as- добавление новой полки для документов
    d - удаление информации о документе
    m - переместить документ на другую полку
    h - помощь (список команд)
    q - завершение работы команды
""")

def main():
    cmd = ''
    print('Введите команду в формате:', end = '')
    print(HELP_STRING)
    
    # p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    # s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    # l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    # a – add – команда, которая добавит новый документ в каталог и в перечень полок;
    # as – add shelf – команда, которая добавит новую полку;
    # d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.;
    # m - move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    # h - help - выводит список команд с пояснениями;
    # q - quit - завершение работы с программой;

    while cmd != 'q':
        cmd = input('Команда >> ')
        if cmd == 'p':
            # поиск человека по номеру документа
            print('Введите номер документа: ', end = '')
            name = find_people(input())
            if name != '':
                print(f'Документ принадлежит {name}')
            else:
                print('Документ не найден!')
        elif cmd == 's':
            # поиск расположения документа
            print('Введите номер документа: ', end = '')
            dir = find_dir(input())
            if dir != '':
                print(f'Документ находится на полке № {dir}')
            else:
                print('Документ не найден!')
        elif cmd == 'l':
            # вывод списка всех хранящихся докуметов
            print('Список хранящихся документов:')
            for doc in documents:
                print(f"""{doc['type']} "{doc['number']}" "{doc['name']}" """)
        elif cmd == 'a':
            # добавление докуметов на хранение
            print('Введите данные нового документа:')
            dtype = input('Тип документа: ')
            dnumber = input('Номер документа: ')
            dname = input('Имя и Фамилия владельца: ')
            ddir = input(f'Номер полки хранения {list(directories.keys())}: ')
            # проверка документа по номеру на дубль и корректности номера полки хранения
            if find_dir(dnumber) != '' or find_people(dnumber) != '':
                print(f'Документс таким номером № {dnumber} уже существует! Данные не сохранены!')
            elif ddir not in list(directories.keys()):
                print(f'Полка хранения № {ddir} не найдена! Данные не сохранены!')
            else:
                documents.append({'type': dtype, 'number': dnumber, 'name': dname})
                directories[ddir].append(dnumber)
        elif cmd == 'as':
            # добавление новой полки хранения
            ddir = input('Введите новый номер полки хранения : ')
            if ddir in list(directories.keys()):
                print(f'Полка хранения № {ddir} уже существует!')
            else:
                directories[ddir] = []
        elif cmd == 'h':
            print('Допустимые команды:', end = '')
            print(HELP_STRING)
        elif cmd == 'd':
            # удаление информации о документе
            dnumber = input('Введите номер документа для удаления: ')
            if find_dir(dnumber) == '' or find_people(dnumber) == '':
                print('Документ не найден!')        
            else:
                if input(f'Удалить сведения о документе {dnumber}? (y/n): ') == 'y':
                    del_document(dnumber)
                    print(f'Сведения о документе № {dnumber} удалены!')
                else:
                    print('Операция отменена!')
        elif cmd == 'm':
            # перемещение документа на другую полку
            dnumber = input('Введите номер документа для перемещения: ')
            ddir = input('Введите номер полки: ')
            if find_people(dnumber) == '':
                print('Документ не найден!')
            elif ddir not in directories:
                print('Неправильно указан номер полки!')
            elif find_dir(dnumber) == ddir:
                print(f'Документ уже находится на полке № {ddir} !')
            else:
                mov_document(dnumber, ddir)
        elif cmd == 'q':
            print('Работа программы завершена!')
        else:
            print('Ошибочная команда, допустимы повторите ввод!')
#end main()

#
# Основная программа
#

if __name__ == '__main__':
    main()

# Конец программы
