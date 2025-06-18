import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "ft_isdigit"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_isdigit.c main.c"

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

def random_digit():
    return random.choice(string.digits)

def random_non_digit():
    return random.choice(string.ascii_letters + string.punctuation + string.whitespace)

def basic_test():
    c = "49"
    return create_test(c)

def non_digit_test():
    c = "41"
    return create_test(c)

def ascii_edge_test():
    c = "48"
    return create_test(c)

def negative_input_test():
    c = "60"
    return create_test(c)

def large_ascii_test():
    c = "136"
    return create_test(c)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: non_digit_test,
        3: ascii_edge_test,
        4: negative_input_test,
        5: large_ascii_test,
    }
    gen_tests(tests)