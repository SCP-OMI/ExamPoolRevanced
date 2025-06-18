import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_strstr"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_strstr.c main.c"

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
    cmd = '"there is uniform selection from a range" "uniform"'
    return create_test(cmd)

def full_string_test():
    cmd = '"Initialize the random number generator." "Initialize"'
    return create_test(cmd)

def no_occurrence_test():
    cmd = '"The following function generates a discrete distribution" "hello"'
    return create_test(cmd)

def substring_at_start_test():
    cmd = '"the corresponding variables in the distributions equation" "variables"'
    return create_test(cmd)

def empty_string_test():
    cmd = '"Weibull distribution. alpha is the scale parameter and beta is the shape parameter" " "'
    return create_test(cmd)

def special_characters_test():
    cmd = '"Sometimes it is useful to be able to reproduce the sequences given by a pseudo-random number generator" "pseudo-random"'
    return create_test(cmd)

def single_character_test():
    cmd = '"there is uniform selection from a range" "f"'
    return create_test(cmd)

def whitespace_string_test():
    cmd = '"Simulation of arrival times and service deliveries for a multiserver queue" " "'
    return create_test(cmd)


if __name__ == "__main__":
    tests = {
        1: basic_test,
        2: full_string_test,
        3: no_occurrence_test,
        4: substring_at_start_test,
        5: empty_string_test,
        6: special_characters_test,
        7: single_character_test,
        8: whitespace_string_test,
    }
    gen_tests(tests)
