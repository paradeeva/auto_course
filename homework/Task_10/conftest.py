
import pytest
from datetime import datetime

@pytest.fixture()
def start_end_time():
    start_time = datetime.now()
    print(f'\n Начало выполнения {start_time}')
    yield
    end_time = datetime.now()
    print(f'\n Конец выполнения {end_time}')

@pytest.fixture()
def duration_time():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    our_time = end_time - start_time
    print(f"\n Время выполнения {our_time}")
