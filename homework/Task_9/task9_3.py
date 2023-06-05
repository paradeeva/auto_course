# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

def read_file(file_name):
    """
    Открывает и читает файл
    :param file_name: путь до файла, который открываем для чтения
    :return: text возвращаемое содержание открытого файла
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def process_file_content(content1):
    """
    Преобразует содержимое файла
    :param content1: получает содержимое файла
    :return: purchases возвращает список покупок, преобразованный из строки в список из целых чисел
    """
    purchases = content1.split("\n\n")
    purchases = [list(map(int, purchase.split('\n'))) for purchase in purchases if purchase]
    return purchases


def get_three_most_expensive_purchases(purchases):
    """
    Выбирает три самые дорогие покупки
    :param purchases: получаемый список покупок
    :return: возвращает после сортировки от большего к меньшему список из трех первых покупок
    """
    purchases.sort(key=sum, reverse=True)
    return purchases[:3]


def calculate_total_cost(purchases):
    """
    Вычисляет общую стоимость покупок
    :param purchases: получает список покупок
    :return: total_cost стоимость покупок
    """
    total_cost = sum(sum(purchase) for purchase in purchases)
    return total_cost


file_name = 'test_file/task_3.txt'
content = read_file(file_name)
purchases = process_file_content(content)
three_most_expensive_purchases1 = get_three_most_expensive_purchases(purchases)
three_most_expensive_purchases = calculate_total_cost(three_most_expensive_purchases1)
print(three_most_expensive_purchases)


assert three_most_expensive_purchases == 202346
