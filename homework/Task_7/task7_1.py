# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False


# Здесь пишем код
import math


class Segment:
    """
    Возвращает длину отрезка, вичисленную по координатам
    """

    def __init__(self, tuple_1, tuple_2):
        """
        Инициализирует атрибуты
        """
        self.tuple_1 = tuple_1
        self.tuple_2 = tuple_2

    def length(self):
        """
        Вычисляет длину отрезка по координатам и округляет до 2х знаков после запятой
        :return length_segment: длина отрезка
        """
        x1 = self.tuple_1[0]
        y1 = self.tuple_1[1]
        x2 = self.tuple_2[0]
        y2 = self.tuple_2[1]
        length_segment = math.hypot(x2 - x1, y2 - y1)
        length_segment = round(length_segment, 2)
        return length_segment

    def x_axis_intersection(self):
        """
        возвращает True, если отрезок пересекает ось абцисс, иначе False
        :return: bool()
        """
        y1 = self.tuple_1[1]
        y2 = self.tuple_2[1]
        return (y2 > 0 > y1) or (y1 > 0 > y2)

    def y_axis_intersection(self):
        """
        возвращает True, если отрезок пересекает ось ординат, иначе False
        :return: bool()
        """
        x1 = self.tuple_1[0]
        x2 = self.tuple_2[0]
        return (x2 > 0 > x1) or (x1 > 0 > x2)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
