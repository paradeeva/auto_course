# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


import pytest
from datetime import datetime


class TestTask4:

    @pytest.fixture()
    def start_time_all_tests(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time = "All tests in class start in time =" + str(current_time)
        yield current_time

    @pytest.fixture()
    def end_time_all_tests(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time = "All tests in class finish in time =" + str(current_time)
        yield current_time
        print(current_time)

    @pytest.fixture()
    def start_end_time_test(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time = "Test start in time =" + str(current_time)
        yield current_time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time = "Test finish in time =" + str(current_time)
        print(current_time)

    def all_division(self, *arg1):
        if len(arg1) == 0:
            try:
                raise IndexError('tuple index out of range')
            except Exception:
                return ('tuple index out of range')
        division = arg1[0]
        for i in arg1[1:]:
            if i == 0:
                try:
                    raise Exception('division by zero')
                except Exception:
                    return ('division by zero')
            division /= i
        return division

    def test1_two_args(self, start_time_all_tests, start_end_time_test):
        print(start_time_all_tests)
        print("test1_two_args")
        print(start_end_time_test)
        assert self.all_division(10, 5) == 2

    def test1_three_args(self):
        assert self.all_division(20, 4, 2) == 2.5

    def test3_division_by_zero(self):
        assert self.all_division(1, 0) == 'division by zero', 'division by zero'

    def test_with_negative_numbers(self):
        assert self.all_division(-100, -200) == 0.5

    def test_no_args(self, end_time_all_tests):
        assert self.all_division() == 'tuple index out of range', 'tuple index out of range'
        print(end_time_all_tests)
