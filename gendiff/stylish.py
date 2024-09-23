from parcer_file_extension import parse_file
from generate_interior_space import generate_interior_space

def stylish(dict1, dict2, interior_space, depth=1):
    result = []
    indent = depth * '....'
    total_keys = dict1.keys() | dict2.keys()  # Объединяем ключи обоих словарей

    for key in total_keys:
        if key in dict1 and key not in interior_space:
            # Если ключ есть только в dict1 и не отмечен в interior_space
            result.append(f'{indent}{key}: {dict1[key]}')

        if key in interior_space:
            if interior_space[key] == 'deleted':
                result.append(f'{indent[2:]}- {key}: {dict1[key]}')
            elif interior_space[key] == 'changed':
                result.append(f'{indent[2:]}- {key}: {dict1[key]}')
                result.append(f'{indent[2:]}+ {key}: {dict2[key]}')
            elif interior_space[key] == 'added':
                result.append(f'{indent[2:]}+ {key}: {dict2[key]}')

        # Проверка вложенных словарей
        if isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
            nested_result = stylish(dict1[key], dict2[key], interior_space, depth + 1)
            if nested_result:  # Проверяем, что nested_result не пуст
                result.extend(nested_result)

    for i in result:
        print(i)

path1 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.json'
path2 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.json'

dict1 = parse_file(path1)
dict2 = parse_file(path2)


interior_space = generate_interior_space(dict1, dict2)

print(stylish(dict1, dict2, interior_space))
