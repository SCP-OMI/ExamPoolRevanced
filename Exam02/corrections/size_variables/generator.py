import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Raiteb Ahlam'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "size_variable"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "size_variable.c"

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

def random_string(length=10):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))

def int_test():
    return create_test("int")

def char_test():
    return create_test("char")

def empty_string_test():
    return create_test("")

def float_test():
    return create_test("float")

def double_test():
    return create_test("double")

def edge_case_test():
    string = random_string(20) + "!@#$%^&*()"
    return create_test(string)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: int_test,
        2: char_test,
        3: empty_string_test,
        4: float_test,
        5: double_test,
        6: edge_case_test
    }
    gen_tests(tests)