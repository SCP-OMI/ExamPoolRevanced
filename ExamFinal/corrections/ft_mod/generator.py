import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_mod.c main.c"

def compile_expected_program():
    command = f"{COMPILER} {FLAGS} {SRC} -o {EXP_BIN_NAME}"
    call(command, shell=True)

def run_test(value, divisor):
    expected = value if divisor == 0 else value % divisor
    cmd = f"./{EXP_BIN_NAME} {value} {divisor}"
    output = check_output(cmd, shell=True).decode("utf-8").strip()
    return {
        "cmd": cmd,
        "expected": f"{expected}",
    }

def basic_test():
    return run_test(42, 5)

def zero_divisor_test():
    return run_test(100, 0)

def negative_divisor_test():
    return run_test(15, -4)

def zero_value_test():
    return run_test(0, random.randint(1, 10))

def large_numbers_test():
    return run_test(random.randint(1000, 10000), random.randint(1, 100))

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: zero_divisor_test,
        3: negative_divisor_test,
        4: zero_value_test,
        5: large_numbers_test
    }
    gen_tests(tests)
