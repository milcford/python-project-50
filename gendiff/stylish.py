from diff import diff
from parcer_file_extension import parse_file


# diff в данном случае это готовый словарь, depth это глубина которая будет увеличиваться
# когда будет происходить рекурсивный вызов
def stylish(diff, depth=1):

    result = []
    indent = depth * '....'

    for key in diff:
        if diff[key]['status'] == 'added':
            result.append(f'{indent[2:]}+.{key}: {diff[key]['value']}')
        elif diff[key]['status'] == 'deleted':
            result.append(f'{indent[2:]}-.{key}: {diff[key]['value']}')
        elif diff[key]['status'] == 'changed':
            result.append(f'{indent[2:]}-.{key}: {diff[key]['old_value']}')
            result.append(f'{indent[2:]}-.{key}: {diff[key]['new_value']}')
        elif diff[key]['status'] == 'without_changes':
            result.append(f'{indent}{key}: {diff[key]['value']}')
        if diff[key]['status'] == 'nested':
            temp = stylish(diff[key]['nested_changes'], depth = depth + 1)
            result.append(temp)

    print(result)

dict1 = parse_file('/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.json')
dict2 = parse_file('/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.json')

diff = diff(dict1, dict2)

stylish(diff)
