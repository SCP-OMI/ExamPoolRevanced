import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import (
    gen_tests,
    random_word,
    random_words,
    quote,
    quotelist,
    nl,
)

__author__ = 'Mohamed Babela'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "fix_parser.c main.c"

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

def valid_expression_test():
    valid_exprs = [
        "5+3",
        "10-2*3",
        "4 * 5 + 6",
        "123",
        "7/3+9*2",
        "1 + 2 + 3",
        "5*6/2"
    ]
    expr = random.choice(valid_exprs)
    return {
        "cmd": quote(expr),
        "output": "Valid"
    }

def invalid_expression_test():
    invalid_exprs = [
        "5++3",
        "abc",
        "1 + * 2",
        "12@34",
        "5 + a",
        "3 * * 4",
        "x + y"
    ]
    expr = random.choice(invalid_exprs)
    return {
        "cmd": quote(expr),
        "output": "Invalid"
    }

def edge_case_test():
    cases = [
        ("", "Invalid"),
        ("   ", "Invalid"),
        ("5 ", "Valid"),
        (" + 5", "Invalid"),
        ("5 + ", "Invalid"),
        ("(5+3)", "Invalid"),
        ("5.3", "Invalid")
    ]
    expr, expected = random.choice(cases)
    return {
        "cmd": quote(expr),
        "output": expected
    }

def random_expression_test():
    chars = string.digits + "+-*/ "
    length = random.randint(1, 10)
    expr = ''.join(random.choice(chars) for _ in range(length))

    is_valid = True
    if not expr or not expr[0].isdigit():
        is_valid = False
    for i in range(len(expr)):
        if expr[i] not in chars:
            is_valid = False
        if i > 0 and expr[i] in "+-*/" and expr[i-1] in "+-*/":
            is_valid = False
    return {
        "cmd": quote(expr),
        "output": "Valid" if is_valid else "Invalid"
    }

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: valid_expression_test,
        2: invalid_expression_test,
        3: edge_case_test,
        "4-10": valid_expression_test,
        "11-15": invalid_expression_test,
        "16-20": edge_case_test,
        "21-30": random_expression_test,
    }
    gen_tests(tests)