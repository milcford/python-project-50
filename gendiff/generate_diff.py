def generate_diff(file1, file2):
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
