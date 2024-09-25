from parcer_file_extension import parse_file


def diff(dict1, dict2):
    result = {}

    for key in dict1:
        if key not in dict2:
            result[key] = {
                'status': 'deleted',
                'value': dict1[key]
            }
        else:
            if dict1[key] == dict2[key]:
                result[key] = {
                    'status': 'without_changes',
                    'value': dict1[key]
                }
            elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                nested_changes = diff(dict1[key], dict2[key])
                if nested_changes:
                    result[key] = nested_changes
                else:
                    result[key] = {
                        'status': 'without_changes',
                        'value': dict1[key]
                    }
            else:
                result[key] = {
                    'status': 'changed',
                    'old_value': dict1[key],
                    'new_value': dict2[key]
                }

    for key in dict2:
        if key not in dict1:
            result[key] = {
                'status': 'added',
                'value': dict2[key]
            }

    return result

path1 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.json'
path2 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.json'
# Получаем наши готовые словари для сравнения с помощью функции parse_file
p1 = parse_file(path1)
p2 = parse_file(path2)
print(diff(p1, p2))
