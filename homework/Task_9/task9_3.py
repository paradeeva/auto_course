# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
# Функция для чтения файла
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # открываем файл для чтения
        content = f.read()  # считываем содержимое файла
    return content  # возвращаем содержимое файла

# Функция для обработки содержимого файла
def process_file_content(content):
    purchases = content.split("\n\n")  # разделяем покупки по пустым строкам
    # конвертируем строковые значения цен в целые числа
    purchases = [list(map(int, purchase.split('\n'))) for purchase in purchases if purchase]
    return purchases  # возвращаем список покупок

# Функция для получения трех самых дорогих покупок
def get_three_most_expensive_purchases(purchases):
    # сортируем покупки по сумме цен, начиная с самой высокой
    purchases.sort(key=sum, reverse=True)
    return purchases[:3]  # возвращаем три самые дорогие покупки

# Функция для подсчета общей стоимости покупок
def calculate_total_cost(purchases):
    # вычисляем общую стоимость покупок
    total_cost = sum(sum(purchase) for purchase in purchases)
    return total_cost  # возвращаем общую стоимость

# Название файла
filename = 'test_file/task_3.txt'
# filename = 'C:/Users/nm.paradeeva/PycharmProjects/homeWork1/Task_9/task_3.txt'

# Читаем содержимое файла
content = read_file(filename)
# Обрабатываем содержимое файла
purchases = process_file_content(content)
# Получаем три самые дорогие покупки
three_most_expensive_purchases1 = get_three_most_expensive_purchases(purchases)
# Вычисляем общую стоимость покупок
three_most_expensive_purchases = calculate_total_cost(three_most_expensive_purchases1)

# Выводим результат на экран
print(three_most_expensive_purchases)


assert three_most_expensive_purchases == 202346