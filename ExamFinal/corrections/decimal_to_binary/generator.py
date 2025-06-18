import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "decimal_to_binary.c"

def compile_expected_program():
    command = f"{COMPILER} {FLAGS} {SRC} -o {EXP_BIN_NAME}"
    call(command, shell=True)
def create_test(cmd):
    output = check_output(f"./{EXP_BIN_NAME} {cmd}", shell=True).decode('utf-8').strip()
    return {
        "cmd": cmd,
        "output": output,
    }

def decimal_to_binary(n):
    return bin(n)[2:]
def valid_decimal_test():
    return create_test("96")

def invalid_input_test():
    return create_test("5")

def no_argument_test():
    return create_test("")

def too_many_arguments_test():
    return create_test("8613")

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: valid_decimal_test,
        "2-6": invalid_input_test,
        7: no_argument_test,
        8: too_many_arguments_test,
    }
    gen_tests(tests)
