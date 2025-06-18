import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import (
    gen_tests,
    quote,
)

__author__ = 'Ahlam Raiteb'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "prev_character.c"

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
    return create_test("a")

def basic_test1():
    return create_test("Z")

def random_character():
    char = random.choice(string.printable.strip())
    return create_test(quote(char))

def empty_test():
    return create_test("")

def multiple_arguments_test():
    chars = " ".join(quote(random.choice(string.ascii_letters)) for _ in range(random.randint(2, 5)))
    return create_test(chars)
    

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: multiple_arguments_test,
        3: empty_test,
        4: basic_test1,
        "5-20": random_character,
    }
    gen_tests(tests)