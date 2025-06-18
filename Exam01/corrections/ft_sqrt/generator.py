import random
import math
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_sqrt"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_sqrt.c main.c"

def compile_expected_program():
    command = "{compiler} {flags} {src} -o {bin_name}" \
        .format(compiler=COMPILER,
                flags=FLAGS,
                src=SRC,
                bin_name=EXP_BIN_NAME)
    call(command, shell=True)

def create_test(cmd):
    output = check_output(f"./{EXP_BIN_NAME} {cmd}", shell=True)
    return {
        "cmd": cmd,
        "output": output.decode('utf-8'),
    }

def basic_square_root():
    number = 4
    return create_test(number)

def perfect_square():
    number = 49
    return create_test(number)

def non_perfect_square():
    number = 1
    return create_test(number)

def edge_case_zero():
    number = 0
    return create_test(number)
def edge_case_negative():
    number = 64
    return create_test(number)

def large_perfect_square():
    number = 81
    return create_test(number)

def large_non_perfect_square():
    number = 25
    return create_test(number)

if __name__ == "__main__":
    tests = {
        1: basic_square_root,
        2: perfect_square,
        3: non_perfect_square,
        4: edge_case_zero,
        5: edge_case_negative,
        6: large_perfect_square,
        7: large_non_perfect_square,
    }
    gen_tests(tests)
