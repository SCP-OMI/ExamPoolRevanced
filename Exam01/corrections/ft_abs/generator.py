import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_abs"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_abs.c main.c"

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

def test_positive_number():
    n = "25"
    return create_test(n)

def test_negative_number():
    n = "-8"
    return create_test(n)

def test_zero():
    n = "0"
    return create_test(n)

def test_large_positive():
    n = "1"
    return create_test(n)

def test_large_negative():
    n = "-963"
    return create_test(n)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: test_positive_number,
        2: test_negative_number,
        3: test_zero,
        4: test_large_positive,
        5: test_large_negative,
    }
    gen_tests(tests)