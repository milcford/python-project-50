
def generate_diff(file1, file2):
    # Будем собирать результат в список, потом соединим его с помощью '\n'.join(result)
    result = []
    # Сперва мы проверяем данные в первом файле, они должны идти в итоговом результате первыми в очереди
    # и иметь знак минус (-) перед ключем, если значения у одинаковых ключей разные
    for i in file1:
        # Проверяем есть ли ключи из первого файла во втором
        if i in file2:
            # Проверяем одинаковые ли значения у ключей (выше)
            if file1[i] == file2[i]:
                result.append(f'  {i}: {file1[i]}')  # Done
                # Проверяем что получается
                # print(result)
                # Старый вариант
                # result['  ' + i] = file1[i]
            # Проверяем что бы значения были разными
            if file1[i] != file2[i]:
                result.append(f'- {i}: {file1[i]}') # Done
                # Старый вариант
                # result['- ' + i] = file1[i]
        # Проверяем ключи из первого файла, что бы их не было во втором
        if i not in file2:
            # Если ключа из первого файла нет во втором файле, добавляем его в результат со знаком минус (-)
            result.append(f'- {i}: {file1[i]}') # Done
            # Старый вариант
            # result['- ' + i] = file1[i]
    # Теперь мы проверяем данные из второго файла, если ключи из второго файла есть в первом
    for i in file2:
        # Если ключа нет в первом файле
        if i not in file1:
            # добавляем его в результат со знаком плюс (+)
            result.append(f'+ {i}: {file2[i]}') # Done
            # старый вариант
            # result['+ ' + i] = file2[i]
        # Если ключ есть в первом файле
        if i in file1:
            # если значения по ключу разные
            if file2[i] != file1[i]:
                # добавляем его в результат со знаком плюс (+)
                result.append(f'+ {i}: {file2[i]}')
                # старый вариант
                # result['+ ' + i] = file2[i]
    # print(f'result = {result}') # Смотрим что получилось
    # for i in result:
    #     print(i)
    # Теперь нам надо отсортировать наш результат (список)
    sorted_result = sorted(result, key=lambda x: x[2])
    # Старый вариант сортировки
    # sorted_result = sorted(result.items(), key=lambda x: x[0][2])
    # print(f'Сортированный словарь - {sorted_result}')
    # for i in sorted_result:
    #     print(i)
    # Теперь нам надо собрать текст (строку) из получившегося списка
    result_text = '\n'.join(sorted_result)
    return '{' + '\n' + result_text + '\n' + '}'
    # print('{')
    # for i in sorted_result:
    #     print(f'{i[0]}: {i[1]}')
    # print('}')
    # string_result = [f'{i}: {result[i]}' for i in result]
    # return string_result
    # Надо за результат взять строку и формировать ее, что бы функция возвращала эту строку !!!

# with open('file1.json') as file:
#     data = file.read()
# file1 = json.loads(data)
#
# with open('file2.json') as file:
#     data = file.read()
# file2 = json.loads(data)

# file1 = json.load(open(file='file1.json'))
# # print(f'Первый файл выглядит так - {file1}')
# file2 = json.load(open(file='file2.json'))
# # print(f'Второй файл выглядит так - {file2}')
# print()

# print(generate_diff(file1, file2))
