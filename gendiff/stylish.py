from diff import diff
from parcer_file_extension import parse_file
from make_str import make_str



def stylish(diff, depth=1):
    result = []
    indent = depth * '....'

    for key in diff:
        status = diff[key]['status']
        # Тут надо проверять является ли значение словарем или нет
        if status == 'added':
            if isinstance(diff[key]['value'], dict):
                result.append(f'{indent}{key}:')
                nested_result = stylish(diff[key]['value'], depth + 1)
                result.extend(nested_result)
            result.append(f'{indent[2:]}+ {key}: {make_str(diff[key]["value"])}')
        # Тут также надо проверять является ли значение словарем или нет
        elif status == 'deleted':
            result.append(f'{indent[2:]}- {key}: {make_str(diff[key]["value"])}')
        elif status == 'changed':
            result.append(f'{indent[2:]}- {key}: {make_str(diff[key]["old_value"])}')
            result.append(f'{indent[2:]}+ {key}: {make_str(diff[key]["new_value"])}')
        elif status == 'without_changes':
            result.append(f'{indent}{key}: {make_str(diff[key]["value"])}')
        elif status == 'nested':
            result.append(f'{indent}{key}:')
            nested_result = stylish(diff[key]['nested_changes'], depth + 1)
            result.extend(nested_result)

    return result


dict1 = parse_file('/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.json')
dict2 = parse_file('/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.json')

diff = diff(dict1, dict2)
# print(stylish(diff))
# l = stylish(diff)
#
# for i in l:
#     print(i)

