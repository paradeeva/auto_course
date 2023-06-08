# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_with_negative_number():
    assert all_division(-100, 2, 2) == -25


@pytest.mark.smoke
def test_with_negative_numbers():
    assert all_division(-100, -200, 2) == 0.25


def test_two_args():
    assert all_division(10, 5, 1) == 2


@pytest.mark.smoke
def test_three_args():
    assert all_division(20, 4, 2) == 2.5


@pytest.mark.smoke
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 5, 0)
