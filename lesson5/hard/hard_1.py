# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд(переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл(запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным(full_path) - в Linux начинается с /, в Windows с имени диска
# все остальные пути считать относительными

# Важно! Все операции должны выполняться в той директории, в который вы находитесь. Исходной директорией считать ту,
# в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформеную реализацию.
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("copy - копирование файла")
    print("remove - удаление файла")
    print("cd - смена директории на")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_py():
    print(os.listdir())
    c = input("Какой файл вы бы хотели копировать:")
    try:
        shutil.copy(c, r'copy_{}'.format(c))
    except:
        print("Такого файла не существует")


def remove():
    print(os.listdir())
    c = input("Какую папку удалить?:")
    l = input("Вы точно хотите удалить файл Y/N?")
    if l == 'Y' or l == 'y' :
        try:
            os.removedirs(c)
            print("Ваша папка {} успешно удалена".format(c))
        except:
            print("Такой папки не существует")
    elif l=="N"or l=='n':
        print("Вы вышли из программы")


def cd():
    c = input('Введите путь нужной директории')
    try:
        os.chdir(c)
        print("Вы перешли")
    except:
        print("Невозможно перейти")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "copy": copy_py,
    "remove": remove,
    "cd": cd
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")