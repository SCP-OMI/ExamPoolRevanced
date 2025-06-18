import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_pow"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_pow.c main.c"

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

def random_int(min_val=-10, max_val=10):
    return random.randint(min_val, max_val)

def basic_pow():
    ptr_value = random_int(0, 10)
    number = random_int(0, 5)
    cmd = f"\"{ptr_value}\" \"{number}\""
    return create_test(cmd)

def zero_to_power_of():
    ptr_value = 0
    number = random_int(1, 5)
    cmd = f"\"{ptr_value}\" \"{number}\""
    return create_test(cmd)

def one_to_power_of():
    ptr_value = 1
    number = random_int(1, 5)
    cmd = f"\"{ptr_value}\" \"{number}\""
    return create_test(cmd)

def negative_base():
    ptr_value = random_int(-10, -1)
    number = random_int(0, 5)
    cmd = f"\"{ptr_value}\" \"{number}\""
    return create_test(cmd)

def negative_exponent():
    ptr_value = random_int(1, 10)
    number = random_int(-5, -1)
    cmd = f"\"{ptr_value}\" \"{number}\""
    return create_test(cmd)

def large_values():
    ptr_value = random_int(1, 5)
    number = random_int(10, 15)
    cmd = f"\"{ptr_value}\" \"{number}\""
    return create_test(cmd)

def edge_case_zero_exponent():
    ptr_value = random_int(1, 10)
    number = 0
    cmd = f"\"{ptr_value}\" \"{number}\""
    return create_test(cmd)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_pow,
        2: zero_to_power_of,
        3: one_to_power_of,
        4: negative_base,
        5: negative_exponent,
        6: large_values,
        7: edge_case_zero_exponent,
    }
    gen_tests(tests)
