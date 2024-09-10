import argparse
import json
import gendiff.generate_diff

parser = argparse.ArgumentParser()

print('Compares two configuration files and shows a difference.')

# Позиционные аргументы
parser.add_argument('first_file')
parser.add_argument('second_file')

parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()

print(args)

first_file = args.first_file
second_file = args.second_file

with open(f'gendiff/tests/fixtures/{first_file}') as file:
    data = file.read()
file1 = json.loads(data)

with open(f'gendiff/tests/fixtures/{second_file}') as file:
    data = file.read()
file2 = json.loads(data)

diff = gendiff.generate_diff(file1, file2)
print(diff)


