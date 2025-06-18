import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Raiteb Ahlam'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "sort_words"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "sort_words.c"

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

def basic_test():
    string = random_string(30)
    return create_test(string)
def basic_test1():
    string = "Is Are Am"
    return create_test(string)
def basic_test2():
    string = "banana cat apple"
    return create_test(string)
def basic_test3():
    string = "Welcome to the Daily Rundown"
    return create_test(string)

def not_found_test():
    string = random_string(20)
    return create_test(string)

def empty_string_test():
    string = "Forming meaningful relationships"
    return create_test(string)

def first_char_test():
    string = random_string(20)
    return create_test(string)

def last_char_test():
    string = random_string(20)
    return create_test(string)

def edge_case_test():
    string = random_string(20) + "!@#$%^&*()"
    return create_test(string)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: not_found_test,
        3: empty_string_test,
        4: first_char_test,
        5: last_char_test,
        6: edge_case_test,
        7: basic_test1,
        8: basic_test2,
        9: basic_test3
    }
    gen_tests(tests)