from generate_interior_space import generate_interior_space
from parcer_file_extension import parse_file

def stylish(dict1, dict2, interior_space):
    result = []
    # Проходим по нашему внутреннему пространству с состояниями ключей: 'without_changes', 'changed',
    # 'deleted', 'added'
    for key in interior_space:
        # Если ключ без изменений
        if key['without_changes']:
            # Нужно осуществить поиск данного ключа, так как он может быть вложенным
            for i in dict1:
                if key == i:
                    # Добавляем как строку ключ со значением из первого словаря
                    result.append(f'..{key}: {dict1[key]}') # Встроенный словарь
                for j in i:

        if key['changed']:
            result.append(f'-.{key}: {dict1[key]}')
        if key['deleted']:
            result.append(f'-.{key}: {dict1[key]}')
        if key['added']:
            result.append(f'+.{key}: {dict2[key]}')

        return result

        # sorted_result = sorted(result, key=lambda x: x[2])
        # result_text = '\n'.join(sorted_result)
        # return '{' + '\n' + result_text + '\n' + '}'



    # # Проходим по нашему второму словарю (по его ключам)
    # for i in dict2:
    #     # Если ключ из второго словаря отсутствует в первом
    #     if i not in dict1:
    #         # Добавляем этот ключ: значение в наш результат со знаком плюса (Тут необходимо реализовать
    #         # отдельное внутренне представление и отметить что этот ключ был добавлен (т.к. ключ
    #         # присутствует во втором словаре, но отсутствует в первом))
    #         result.append(f'+ {i}: {dict2[i]}')
    #     # Если ключ из второго словаря есть в первом
    #     if i in dict1:
    #         # Если значение по ключу из второго словаря не равно значению такого же ключа из первого словаря
    #         if dict2[i] != dict1[i]:
    #             # Добавляем этот ключ: значение в наш результат со знаком плюса (Тут необходимо реализовать
    #             # отдельное внутренне представление и отметить что этот ключ был изменен (т.к. ключ
    #             # присутствует во втором словаре, но отсутствует в первом))
    #             result.append(f'+ {i}: {dict2[i]}')

    # Получается что у нас есть два варианта изменения ключей если он изменен и имеет знак минус, тогда этот
    # ключ из первого словаря, если ключ изменен и имеет знак плюс тогда этот ключ из второго словаря

    # Попробовать формировать словарь который будет включать в себя ключи, а значением будут выступать
    # состояние этого ключа (добавлен, изменен, удален)

    # sorted_result = sorted(result, key=lambda x: x[2])
    # result_text = '\n'.join(sorted_result)
    # return '{' + '\n' + result_text + '\n' + '}'

path1 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.json'
path2 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.json'

p1 = parse_file(path1)
p2 = parse_file(path2)
interior_space = generate_interior_space(p1, p2)

print(stylish(p1, p2, interior_space))
