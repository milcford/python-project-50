from diff import diff
from parcer_file_extension import parse_file


# ХЗ нужна тут эта сортировка или нет
# total_keys = dict1 | dict2  # Объединяем ключи обоих словарей
# sorted_keys = sorted(total_keys)
def stylish(diff, depth=1):
    # depth += 1
    result = []
    indent = depth * '....'

    # Проходим по всем ключам
    for key in diff:
        # Нужно каким-то образом проверять статус ключа в нашем diff слоавре

        # Если ключ со статусом nested - этот момент наверно надо обрабатывать в конце
        # так как ХЗ почему что бы в рекурсию вызывать в нем с самом конце
        if diff[key]['status'] == 'nested':
            # Добавляем только сам ключ двоеточие и отрытую фигурную скобку: common: {
            result.append(f'{indent}{key}: {{')
            nested_diff = stylish(diff[key]['nested_changes'], depth= depth + 1)
            result.append(nested_diff)
            result.append(f'{indent}}}')

        # Нигде не добавляются сами значения, подумать как их добавлять
        # ПОКА ЧТО В ГОЛОВУ НИЧЕГО НЕ ПРИХОДИТ
        elif diff[key]['status'] == 'without_changed':
            result.append(f'{indent}{key}: {{')

        elif diff[key]['status'] == 'deleted':
            result.append(f'{indent[:-2]}- {key}: {{')

        elif diff[key]['status'] == 'added':
            result.append(f'{indent[:-2]}+ {key}: {{')

        elif diff[key]['status'] == 'changed':
            result.append(f'{indent[:-2]}- {key}: {{')
            result.append(f'{indent[:-2]}+ {key}: {{')

    print(result)

dict1 = parse_file('/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.json')
dict2 = parse_file('/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.json')

diff = diff(dict1, dict2)

stylish(diff)
