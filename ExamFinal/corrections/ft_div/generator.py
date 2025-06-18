# !/usr/bin/env python

from subprocess import call, check_output
from deepthought.correction.tests import gen_tests
import random

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_div"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_div.c main.c"

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

def random_int(min_val=-1000, max_val=1000):
    return random.randint(min_val, max_val)

def random_positive_int(min_val=1, max_val=1000):
    return random.randint(min_val, max_val)

def basic_division():
    ptr_value = random_int()
    divisor = random_positive_int()
    cmd = f"\"{ptr_value}\" \"{divisor}\""
    return create_test(cmd)
   

def division_by_one():
    ptr_value = random_int()
    divisor = "1"
    cmd = f"\"{ptr_value}\" \"{divisor}\""
    return create_test(cmd)

def division_by_zero():
    ptr_value = random_int()
    divisor = "0"
    cmd = f"\"{ptr_value}\" \"{divisor}\""
    return create_test(cmd)

def negative_numbers():
    ptr_value = random_int(-1000, 0)
    divisor = random_positive_int()
    cmd = f"\"{ptr_value}\" \"{divisor}\""
    return create_test(cmd)

def large_values():
    ptr_value = random_int(-10**6, 10**6)
    divisor = random_positive_int(1, 10**6)
    cmd = f"\"{ptr_value}\" \"{divisor}\""
    return create_test(cmd)

def edge_case_large_divisor():
    ptr_value = random_int(-1000, 1000)
    divisor = 10**6
    cmd = f"\"{ptr_value}\" \"{divisor}\""
    return create_test(cmd)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_division,
        2: division_by_one,
        3: division_by_zero,
        4: negative_numbers,
        5: large_values,
        6: edge_case_large_divisor,
    }
    gen_tests(tests)




