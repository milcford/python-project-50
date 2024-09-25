from diff import diff

def stylish(diff, depth=1):
    result = []
    indent = depth * '....'
    total_keys = dict1 | dict2  # Объединяем ключи обоих словарей
    sorted_keys = sorted(total_keys)

    # Проходим по всем ключам
    for key in sorted_keys:
        # Если ключ есть
        if key in diff and key not in interior_space:
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

dict1 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.json'
dict2 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.json'


diff = diff(dict1, dict2)

print(stylish(diff))
