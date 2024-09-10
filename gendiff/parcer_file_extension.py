import json
import yaml


def parse_file(path):
    # Открываем файл
    with open(path) as file:
        # Присваиваем прочтенные данные в переменную
        content = file.read()
    # Если контента нет
    if not content:
        # Вызываем ошибку 'Empty file'
        raise ValueError('Empty file')
    # Ищем индекс точки справа у имени файла
    last_dot_index = path.rfind('.')
    # Присваиваем в переменную расширение файла, к найденному индексу +1 и идем до конца, тем самым получая расширение
    file_extension = path[last_dot_index + 1:]
    # Если расширение файла равно 'yml'
    if file_extension == 'yml' or 'yaml':
        # Переопределяем расширение файла в 'yaml'
        file_extension = 'yaml'
    # Проверка расширения файла
    match file_extension:
        # Если расширение 'json'
        case 'json':
            # Возвращаем преобразованный json файл (как словарь)
            return json.loads(content)
        # Если расширение 'yaml'
        case 'yaml':
            # Возвращаем преобразованный yaml файл (как словарь)
            return yaml.safe_load(content)
        # Если расширение не определено
        case _:
            # Возвращаем ошибку
            raise NameError(f'file extension {file_extension} not supported')

# file = '/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.yaml'
# print(parse_file(file))
