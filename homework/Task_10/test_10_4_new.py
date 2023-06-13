# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('start_end_time')
class TestTask4:

    def test_with_negative_number(self):
        assert all_division(-100, 2, 2) == -25

    def test_with_negative_numbers(self):
        assert all_division(-100, -200, 2) == 0.25

    def test_two_args(self, duration_time):
        assert all_division(10, 5, 1) == 2

    def test_three_args(self):
        assert all_division(20, 4, 2) == 2.5
