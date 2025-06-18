import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "ahlam.raiteb@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "triangle_area.c main.c"

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

def basic_test():
    cmd = '"2" "3"'
    return create_test(cmd)

def decimal_test():
    cmd = '"12" "15"'
    return create_test(cmd)

def zero_test():
    cmd = '"0" "3"'
    return create_test(cmd)

def large_radius_test():
    cmd = '"251" "31"'
    return create_test(cmd)

def negative_radius_test():
    cmd = '"-9" "-2"'
    return create_test(cmd)

def negative_positive_radius_test_1():
    cmd = '"-1" "3"'
    return create_test(cmd)

def negative_positive_radius_test_2():
    cmd = '"2" "-12"'
    return create_test(cmd)


if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1 : basic_test,
        2 : decimal_test,
        3: zero_test,
        4 : large_radius_test,
        5 : negative_radius_test,
        6 :negative_positive_radius_test_1,
        7 :negative_positive_radius_test_2,
       
    }
    gen_tests(tests)