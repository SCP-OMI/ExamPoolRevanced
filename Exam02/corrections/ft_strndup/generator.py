import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_strndup"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_strndup.c main.c"

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
    cmd = '"lIA agentique au déploiement industriel" "20"'
    return create_test(cmd)

def full_string_test():
    cmd = '"hello" "5"'
    return create_test(cmd)

def zero_n_test():
    cmd = '"Initialize the random number generator" "0"'
    return create_test(cmd)

def large_n_test():
    cmd = '"Returns a new list containing elements from the population while leaving the original population unchanged" "45"'
    return create_test(cmd)

def empty_string_test():
    cmd = '"" "5"'
    return create_test(cmd)

def special_characters_test():
    cmd = '"pseudo-//random~+**$ number generator." "20"'
    return create_test(cmd)

def single_character_test():
    cmd = '"l" "1"'
    return create_test(cmd)


if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: full_string_test,
        3: zero_n_test,
        4: large_n_test,
        5: empty_string_test,
        6: special_characters_test,
        7: single_character_test
    }
    gen_tests(tests)
