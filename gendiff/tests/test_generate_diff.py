from gendiff import generate_diff
from gendiff.tests.fixtures.result_string import result_string
import json

# with open('gendiff/tests/fixtures/file1.json') as file:
#     data = file.read()
# file1 = json.loads(data)
#
# with open('gendiff/tests/fixtures/file2.json') as file:
#     data = file.read()
# file2 = json.loads(data)


def test_generate_diff():
    assert generate_diff(file1, file2) == result_string
