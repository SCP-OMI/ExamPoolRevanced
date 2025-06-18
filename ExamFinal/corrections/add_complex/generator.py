import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "add_complex.c"

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
    
def  basic_test():
    cmd = '"2" "1" "6" "9"'
    return create_test(cmd)

def  basic_test1():
    cmd = '"6" "4" "3" "2"'
    return create_test(cmd)

def  basic_test2():
    cmd = '"-8" "3" "9" "-6"'
    return create_test(cmd)

def  basic_test3():
    cmd = '"2" "0" "6" "0"'
    return create_test(cmd)

def  basic_test3():
    cmd = '"2" "4" "6" "0"'
    return create_test(cmd)

def  basic_test4():
    cmd = '"" "" "" ""'
    return create_test(cmd)

def  basic_test5():
    return create_test("")

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1 : basic_test,
        2 : basic_test1,
        3 : basic_test2,
        4 : basic_test3,
        5 : basic_test4,
        6 : basic_test5,
    }
    gen_tests(tests)