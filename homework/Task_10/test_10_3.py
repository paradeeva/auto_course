# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args1, args2, args3, result', [
    (100, 2, 2, 25),
    pytest.param(100, 200, 2, 0.25, marks=pytest.mark.smoke),
    (10, 5, 1, 2,),
    (20, 4, 2, 2.5),
    pytest.param(1, 5, 0, 'ZeroDivisionError', marks=pytest.mark.skip('bad'))
])
def test(args1, args2, args3, result):
    assert all_division(args1, args2, args3) == result
