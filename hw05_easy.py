
__author__ = 'Белинский Андрей Петрович'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
from shutil import copyfile


def make_dir(name='New_dir'):
    return os.mkdir(name)


def make_dir_9(n=10):
    try:
        for i in range(1, n):
            name_dir = 'dir_' + str(i)
            make_dir(name_dir)
        return 'Директории созданы успешно'
    except FileExistsError:
        return 'Такие директории уже существуют'


def remove_dir(name):
    return os.rmdir(name)


def remove_dir_9():
    try:
        for i in range(1, 10):
            name_rem_dir = 'dir_' + str(i)
            remove_dir(name_rem_dir)
        return 'Директории успешно удалены'
    except FileNotFoundError:
        return 'Таких директорий не существует'


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir(path_dir='.'):
    return os.listdir(path_dir)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_this_file():
    return copyfile(__file__, __file__[:-3] + '_copy' + __file__[-3:])


if __name__ == "__main__":
    print(make_dir_9())
    print(remove_dir_9())
    print(list_dir())
    print(copy_this_file())