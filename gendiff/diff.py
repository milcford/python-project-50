from parcer_file_extension import parse_file


def diff(dict1, dict2):
    result = {}

    for key in dict1:
        if key not in dict2:
            result[key] = 'deleted'
        else:
            if dict1[key] == dict2[key]:
                result[key] = 'without_changes'
            elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                nested_changes = diff(dict1[key], dict2[key])
                result.update(nested_changes)
            else:
                result[key] = 'changed'

    for key in dict2:
        if key not in dict1:
            result[key] = 'added'

    return result


path1 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.json'
path2 = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.json'
# Получаем наши готовые словари для сравнения с помощью функции parse_file
# p1 = parse_file(path1)
# p2 = parse_file(path2)
# print(generate_interior_space(p1, p2))
