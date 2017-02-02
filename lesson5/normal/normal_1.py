# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов: 1, 3,4, программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"

# Для решения данной задачи используйте алоритмы из задания easy,
# оформленныйе в виде соответствующих функций, и импортированные в данный файл из easy.py
import os
import sys
sys.path.append('D:\git\python\lesson5\easy')
import easy_2
while True:
    a = input("""Выберите действие:
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Удалить папку
    4. Создать папку
    5. Выход
    Выбор:""")

    def konsol(a):
        if a == '1':
            c = input('Введите путь нужной директории')
            try:
                os.chdir(c)
                print("Вы перешли")
            except:
                print("Невозможно перейти")
        elif a == '2':
            easy_2.directoria()
        elif a== '3':
            c = input("Какую папку удалить?:")
            try:
                os.removedirs(c)
                print("Ваша папка {} успешно удалена".format(c))
            except:
                print("Такой папки не существует")
        elif a == '4':
            c = input("Как назвать новую папку?:")
            dir_path = os.path.join(os.getcwd(), c)
            try:
                os.mkdir(dir_path)
                print("Папка {} успешно создана".format(c))
            except:
                print("Такая папка {} уже создана".format(c))

    if a == '5':
        print("Вы вышли")
        break
    konsol(a)