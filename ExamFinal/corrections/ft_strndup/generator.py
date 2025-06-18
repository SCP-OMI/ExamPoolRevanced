import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_strndup"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_strndup.c main.c"

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
def random_string(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def basic_test():
    s = random_string(10)
    n = 5
    expected = s[:n]
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def full_string_test():
    s = random_string(8)
    n = len(s)
    expected = s
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def zero_n_test():
    s = random_string(10)
    n = 0
    expected = ''
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def large_n_test():
    s = random_string(6)
    n = 100
    expected = s
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def empty_string_test():
    s = ""
    n = 5
    expected = ''
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def special_characters_test():
    s = "!@#$%^&*()_+"
    n = 5
    expected = s[:n]
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def single_character_test():
    s = "X"
    n = 1
    expected = "X"
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def whitespace_string_test():
    s = "   \t   "
    n = 4
    expected = s[:n]
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def mixed_case_test():
    s = "AbCdEfGhIj"
    n = 6
    expected = s[:n]
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

def edge_case_n_equals_negative():
    s = random_string(10)
    n = -5
    expected = ''
    return {
        "cmd": f"./ft_strndup \"{s}\" {n}",
        "output": expected
    }

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: full_string_test,
        3: zero_n_test,
        4: large_n_test,
        5: empty_string_test,
        6: special_characters_test,
        7: single_character_test,
        8: whitespace_string_test,
        9: mixed_case_test,
        10: edge_case_n_equals_negative
    }
    gen_tests(tests)
