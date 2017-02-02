# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт
import shutil
def copy_py():
    shutil.copy(r'easy_3.py', r'easy_3_copy.py')
copy_py()
