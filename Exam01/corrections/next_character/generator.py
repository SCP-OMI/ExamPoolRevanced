from subprocess import call, check_output
from deepthought.correction.tests import (
    gen_tests,
)

__author__ = 'Ahlam Raiteb'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "next_character.c main.c"

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
    create_test("Z")

def test1():
    create_test("a")

def test2():
    create_test("P")

def test3():
    create_test("o")

def test4():
    create_test("U")

def test5():
    create_test("B")

def test6():
    create_test("M")

def test7():
    create_test("N")

    

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: test1,
        3: test2,
        4: test3,
        5: test4,
        6: test5,
        7: test6,
        8: test7
    }
    gen_tests(tests)