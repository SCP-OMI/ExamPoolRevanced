import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_bubblesort"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_bubblesort.c main.c"

def compile_expected_program():
    command = f"{COMPILER} {FLAGS} {SRC} -o {EXP_BIN_NAME}"
    call(command, shell=True)
def create_test(cmd):
    output = check_output(f"./{EXP_BIN_NAME} {cmd}", shell=True).decode('utf-8').strip()
    return {
        "cmd": cmd,
        "output": output,
    }

def generate_random_array(size, min_val=-1000, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(size)]

def format_array(arr):
    return ' '.join(map(str, arr))

def test_sorted_array():
    cmd = "1, 2, 3, 4, 5"
    return create_test(cmd)

def test_reverse_sorted_array():
    cmd = "9, 8, 7, 3, 2, -1, -9"
    return create_test(cmd)

def test_random_array():
    cmd = "1, -01, 12, 52, 93, 14, -4, -5"
    return create_test(cmd)

def test_single_element():
    cmd = "5, 3, 9, 7, 6"
    return create_test(cmd)

def test_duplicate_numbers():
    cmd = "1, -01, 12, 52, 93, 14, -4, -59, 8, 7, 3, 2, -1, -9, 1"
    return create_test(cmd)

if __name__ == "__main__":
    tests = {
        1: test_sorted_array,
        2: test_reverse_sorted_array,
        3: test_random_array,
        4: test_single_element,
        5: test_duplicate_numbers,
    }
    gen_tests(tests)