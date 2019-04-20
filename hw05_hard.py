
__author__ = 'Белинский Андрей Петрович'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil


#print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('copy <file_name> - создает копию указанного файла')
    print('remove <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print('chdir <full_path or relative_path> - меняет текущую директорию на указанную')
    print('getcwd - отображение полного пути текущей директории')
    print('listdir - отобразить список файлов в текущей директории')


def make_dir():
    dir_name = input('Введите директорию\n')
    if not dir_name:
        print("Необходимо указать имя директории\n")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
    except PermissionError:
        print('Отказано в доступе')


def ping():
    print("pong")


def copy():
    file_name = input('Введите имя файла\n')
    if not file_name:
        print("Необходимо указать имя файла\n")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    split_path = os.path.splitext(file_path)
    try:
        shutil.copyfile(file_path, os.path.join(os.getcwd(), '{}_copy{}'.format(split_path[0], split_path[1])))
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        print('Отказано в доступе')
    else:
        print('Файл {} успешно скопирован'.format(file_name))


def remove():
    file_name = input('Введите имя файла\n')
    if not file_name:
        print("Необходимо ввести имя файла\n")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        user_ans = input('Вы уверенны, что хотите удалить файл "{}"? [Yes - Y/No - Any]\n'.format(file_name))
        if user_ans.lower() == 'y':
            os.remove(file_path)
        else:
            print('Удаление отменено')
    except FileNotFoundError:
        print('Имя файла указано неверно')
    except PermissionError:
        print('Отказано в доступе')
    else:
        print('Файл {} успешно удален'.format(file_name))


def chdir():
    dir_name = input('Введите директорию\n')
    if not dir_name:
        print("Необходимо указать имя директории\n")
        return
    dir_path = os.path.realpath(dir_name)
    try:
        os.chdir(dir_path)
    except PermissionError:
        print('Отказано в доступе')
    except FileNotFoundError:
        print('Неверное имя директории')
    else:
        print('Директория изменена {}'.format(dir_path))


def getcwd():
    return print(os.getcwd())


def listdir():
    return print(os.listdir(os.getcwd()))


def exit_file():
    return sys.exit()


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "copy": copy,
    "remove": remove,
    "chdir": chdir,
    "getcwd": getcwd,
    "listdir": listdir,
    "q": exit_file
}

while True:
    key = input('')
    if key:
        if do.get(key):
            do[key]()
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None

    try:
        key = sys.argv[1]
    except IndexError:
        key = None

