# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код


import re

fw = open('test_file/task1_answer.txt', 'w', encoding='utf-8')
with open('test_file/task1_data.txt', 'r', encoding='utf-8') as f:
    for i in f:
        tmp = ''
        s1 = re.sub('[0-9]', '', i)
        tmp += s1 + ''
        fw.write(tmp)
    fw.close()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
