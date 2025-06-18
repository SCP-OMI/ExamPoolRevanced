import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_strchr"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_strchr.c main.c"

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
    cmd = '"there is uniform selection from a range" "f"'
    return create_test(cmd)

def not_found_test():
    cmd = '"there is uniform selection from a range" "d"'
    return create_test(cmd)

def empty_string_test():
    cmd = '"Initialize the random number generator." "."'
    return create_test(cmd)

def first_char_test():
    cmd = '"Generate n random bytes." "G"'
    return create_test(cmd)

def last_char_test():
    cmd = '"Returns a non-negative Python integer" "R"'
    return create_test(cmd)

def edge_case_test():
    cmd = '"This method now accepts zero for k" " "'
    return create_test(cmd)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: not_found_test,
        3: empty_string_test,
        4: first_char_test,
        5: last_char_test,
        6: edge_case_test
    }
    gen_tests(tests)