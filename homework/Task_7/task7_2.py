# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056


# Здесь пишем код
class PersonInfo:
    """
    Возвращает строку 'Фамилия И.', путь 'Головное подразделение --> ... --> Конечное подразделение', рассчетное
    значеие зарплаты
    """

    def __init__(self, name_surname, age, department, subdivision='', function='', group=''):
        """
        инициализирует атрибуты
        :param name_surname: имя фамилия
        :param age: возраст
        :param department: отдел
        :param subdivision: подразделение
        :param function: трудовая функция
        :param group: группа
        """
        self.name_surname = name_surname
        self.age = age
        self.department = department
        self.subdivision = subdivision
        self.function = function
        self.group = group

    def short_name(self):
        """
        Преобразует строку 'name_surname'
        :return: short_name строка 'Фамилия И.'
        """
        short_name = self.name_surname
        short_name_list = short_name.split()
        short_name = short_name_list[1] + " " + short_name_list[0][0] + "."
        return short_name
        
    def path_deps(self):
        """
        Возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
        :return: path_deps
        """
        path_deps = self.department
        if len(self.subdivision) > 0:
            path_deps += " --> " + self.subdivision
        if len(self.function) > 0:
            path_deps += " --> " + self.function
        if len(self.group) > 0:
            path_deps += " --> " + self.group
        return path_deps

    def new_salary(self):
        """
        Преобразуем полученные строки в общую строку, создаем словарь (ключ - буква, значение - количество вхождений);
        значения из словаря кладем в список, который сортируем по убыванию
        :return: new_salary рассчитанную по формуле зарплату
        """
        full_work_place = (self.department + self.subdivision + self.function + self.group).replace(" ", "")
        dict_of_letters = {}
        for letter in full_work_place:
            if letter in dict_of_letters.keys():
                dict_of_letters[letter] += 1
            else:
                dict_of_letters[letter] = 1
        result_list = []
        for key in dict_of_letters.keys():
            result_list.append(dict_of_letters[key])
        result_list.sort(reverse=True)
        new_salary = 1337 * self.age * (result_list[0] + result_list[1] + result_list[2])
        return new_salary

    # (регистр имеет значение "А" и "а" - разные буквы)
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
