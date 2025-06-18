from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "decimal_to_binary.c"

def compile_expected_program():
    command = f"{COMPILER} {FLAGS} {SRC} -o {EXP_BIN_NAME}"
    call(command, shell=True)
def create_test(cmd):
    output = check_output(f"./{EXP_BIN_NAME} {cmd}", shell=True).decode('utf-8').strip()
    return {
        "cmd": cmd,
        "output": output,
    }

def test():
    create_test("96")

def test1():
    create_test("5")

def test3():
    create_test("2")

def test2():
    create_test("3")

def test4():
    create_test("12")

def test5():
    create_test("6")

def test6():
    create_test("7")

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: test,
        2: test1,
        3: test2,
        2: test3,
        2: test4,
        7: test5,
        8: test6,
    }
    gen_tests(tests)
