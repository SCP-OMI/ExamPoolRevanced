from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "ahlam.raiteb@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "volume_cube.c main.c"

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
    return create_test("2")

def decimal_test():
    return create_test("22")

def zero_test():
    return create_test("0")

def large_radius_test():
    return create_test("100")

def negative_radius_test():
    return create_test("5")


if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1 : basic_test,
        2 : decimal_test,
        3 : zero_test,
        4 : large_radius_test,
        5 : negative_radius_test
        
    }
    gen_tests(tests)