from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_div"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_div.c main.c"

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
    return create_test('"42" "5"')

def zero_divisor_test():
    return create_test('"100" "0"')

def negative_divisor_test():
    return create_test('"15" "-4"')

def zero_value_test():
    return create_test('"0" "3"')

def large_numbers_test():
    return create_test('"60" "2"')

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: zero_divisor_test,
        3: negative_divisor_test,
        4: zero_value_test,
        5: large_numbers_test
    }
    gen_tests(tests)