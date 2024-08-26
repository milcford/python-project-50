import argparse

parser = argparse.ArgumentParser()

print('Compares two configuration files and shows a difference.')

# Позиционные аргументы
parser.add_argument('first_file')
parser.add_argument('second_file')

parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()

print(args)