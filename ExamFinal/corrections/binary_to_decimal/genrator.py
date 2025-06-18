import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "ahlam.raiteb@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "binary_to_decimal.c"

def compile_expected_program():
    command = f"{COMPILER} {FLAGS} {SRC} -o {EXP_BIN_NAME}"
    call(command, shell=True)

def create_test(cmd):
    output = check_output(f"./{EXP_BIN_NAME} {cmd}", shell=True).decode('utf-8')
    return {
        "cmd": cmd,
        "output": output,
    }

def valid_binary_test():
    return create_test("101")

def invalid_binary_test():
    return create_test("10100000101")

def no_argument_test():
    return create_test("")

def too_many_arguments_test():
    return create_test("101110")

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: valid_binary_test,
        2: invalid_binary_test,
        "3-7": no_argument_test,
        8: too_many_arguments_test,
    }
    gen_tests(tests)
