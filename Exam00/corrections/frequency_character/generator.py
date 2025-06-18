import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import (
    gen_tests,
)

__author__ = 'Ahlam Raiteb'
__email__ = "ahlam.raiteb@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "frequency_character.c main.c"

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
        "output": output,
    }

def random_char():
    return random.choice(string.ascii_letters + string.digits + string.punctuation)

def random_string(length=15):
    return ''.join(random.choice(string.ascii_letters + " ") for _ in range(length))

def basic_test():
    cmd = '"l" "Hello world!"'
    return create_test(cmd)

def no_occurrence_test():
    cmd = '"x" "Hello world!"'
    return create_test(cmd)

def single_occurrence_test():
    cmd = '"H" "Hello world!"'
    return create_test(cmd)

def multiple_occurrences_test():
    cmd = '"p" "Hello world!"'
    return create_test(cmd)

def empty_input_test():
    cmd = '"x" "fsdhshtr xdwsx x"'
    return create_test(cmd)

def wrong_argument_count_test():
    cmd = '"!" "Hello world!"'
    return create_test(cmd)

def multiple_arguments_test():
    cmd = '" " "Hello world!"'
    return create_test(cmd)
    

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: no_occurrence_test,
        3: single_occurrence_test,
        4: multiple_occurrences_test,
        5: empty_input_test,
        6: wrong_argument_count_test,
        7: multiple_arguments_test,
    }
    gen_tests(tests)