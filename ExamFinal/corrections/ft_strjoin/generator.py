import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_strjoin"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_strjoin.c main.c"

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
    s1 = random_string(10)
    s2 = random_string(10)
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def empty_first_string_test():
    s1 = ""
    s2 = random_string(10)
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def empty_second_string_test():
    s1 = random_string(10)
    s2 = ""
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def both_empty_strings_test():
    s1 = ""
    s2 = ""
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def null_first_string_test():
    s1 = "NULL"
    s2 = random_string(10)
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def null_second_string_test():
    s1 = random_string(10)
    s2 = "NULL"
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def edge_case_special_characters_test():
    s1 = "Hello, "
    s2 = "!@#$%^&*()_+"
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def edge_case_large_strings_test():
    s1 = random_string(1000)
    s2 = random_string(1000)
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def long_string_with_empty_second_test():
    s1 = random_string(100)
    s2 = ""
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def long_string_with_empty_first_test():
    s1 = ""
    s2 = random_string(100)
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)


if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: empty_first_string_test,
        3: empty_second_string_test,
        4: both_empty_strings_test,
        5: null_first_string_test,
        6: null_second_string_test,
        7: edge_case_special_characters_test,
        8: edge_case_large_strings_test,
        9: long_string_with_empty_second_test,
        10: long_string_with_empty_first_test
    }
    gen_tests(tests)
