import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "sum_n.c main.c"

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
    return create_test("0")

def basic_test1():
    return create_test("1")

def basic_test2():
    return create_test("12")

def basic_test3():
    return create_test("31")

def valid_test():
    num = random.randint(0, 10)
    cmd = f"{num}"
    return create_test(cmd)



def multiple_arguments_test():
    num = random.randint(0, 5)
    return create_test(num)


if __name__ == "__main__":
    compile_expected_program()
    tests = {
        "1-7": valid_test,
        8: multiple_arguments_test,
        9 : basic_test,
        10 : basic_test1,
        11 : basic_test2,
        12 : basic_test3,
    }
    gen_tests(tests)
