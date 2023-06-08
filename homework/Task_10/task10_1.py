# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
import string


def generate_random_name():
    """
    генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелом
    :return: new_string : выводит строку из двух слов, разделенных пробелом
    """
    alphabet = string.ascii_lowercase
    new_string = ''.join(random.choices(alphabet, k=random.randint(1, 14)))
    new_string += " "
    new_string += ''.join(random.choices(alphabet, k=random.randint(1, 14)))
    print(new_string)


generate_random_name()
generate_random_name()
generate_random_name()
generate_random_name()
generate_random_name()
generate_random_name()
generate_random_name()
generate_random_name()
