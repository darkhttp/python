# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter
def filter(spisok,key):
    '''

    :param spisok:
    :param key:
    :return: отфильтрованный список
    нужен списко и функция в key
    '''
    for x in spisok[:]:
        if eval(key):
            spisok.remove(x)
    return spisok
c = filter([1,2,3,4,5,6,7,8,9,12,32,44],'x%2!=0')
print(c)