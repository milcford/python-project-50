from parcer_file_extension import generate_dict

def generate_diff2(file1, file2):
    result = []
    for i in file1:
        if i in file2:
            if file1[i] == file2[i]:
                result.append(f'  {i}: {file1[i]}')
            if file1[i] != file2[i]:
                result.append(f'- {i}: {file1[i]}')
        if i not in file2:
            result.append(f'- {i}: {file1[i]}')
    for i in file2:
        if i not in file1:
            result.append(f'+ {i}: {file2[i]}')
        if i in file1:
            if file2[i] != file1[i]:
                result.append(f'+ {i}: {file2[i]}')
    sorted_result = sorted(result, key=lambda x: x[2])
    result_text = '\n'.join(sorted_result)
    return '{' + '\n' + result_text + '\n' + '}'

with open('/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file1.yaml') as file:
    data = file.read()
file1 = data

with open('/Users/milcford/hexlet/python-project-50/gendiff/tests/fixtures/file2.yaml') as file:
    data = file.read()
file2 = data

file1 = generate_dict(file1)
file2 = generate_dict(file2)


print(generate_diff2(file1, file2))

