# Игра "Эрудит"
# Нужно написать программу scrabble, которая помогает считать кол-во очков (points), полученное за слово (word)
# По одному очку вы получите за буквы а, в, е=ё, и, н, о, р, с, т.
# Два очка стоит д, к, л, м, п, у.
# Три балла получают за б, г, ь, а также я.
# Четыре балла стоят буквы й, ы.
# 5 очков засчитывается за ж, з, х, ц, ч.
# 6 и 7 очков не предусмотрено.
# Восемь можно получить за букву ф, ш, э, ю.
# 10 баллов стоит буква щ,
# а 15 - ъ
# Например (Ввод --> Вывод):
# курс --> 6 (к=2, у=2, р=1, с=1)


def scrabble(word):
    # Здесь нужно написать код
    """
    Программа scrabble, которая помогает считать количество очков (points), полученное за слово (word)
    :param: (word) слово
    :return: (points) количество очков
    """
    points = 0
    one_point = ['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т']
    two_points = ['д', 'к', 'л', 'м', 'п', 'у']
    three_points = ['б', 'г', 'ь', 'я']
    fore_points = ['й', 'ы']
    five_points = ['ж', 'з', 'х', 'ц', 'ч']
    eight_points = ['ф', 'ш', 'э', 'ю']
    ten_points = ['щ']
    fifteen_points = ['ъ']
    for letter in word:
        if letter in one_point:
            points += 1
        if letter in two_points:
            points += 2
        if letter in three_points:
            points += 3
        if letter in fore_points:
            points += 4
        if letter in five_points:
            points += 5
        if letter in eight_points:
            points += 8
        if letter in ten_points:
            points += 10
        if letter in fifteen_points:
            points += 15
    return points

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = ["курс", 'авеинорстё', 'дклмпeу', 'бгья', 'йы', 'жзхцч', 'фшэю', 'щъ', "карабасбарабас", "околоводопроводного",
        "еженедельное", 'эхоэнцефалограф', 'человеконенавистничество', 'делопроизводительница']

test_data = [6, 10, 12, 12, 8, 25, 32, 25, 21, 26, 20, 54, 34, 36]

for i, d in enumerate(data):
    assert scrabble(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
