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
    to_find = s[:5]
    expected = s[5:] + '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def full_string_test():
    s = random_string(8)
    to_find = s
    expected = s + '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def no_occurrence_test():
    s = random_string(8)
    to_find = "notfound"
    expected = '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def substring_at_start_test():
    s = random_string(8)
    to_find = s[:4]
    expected = s[4:] + '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def empty_string_test():
    s = ""
    to_find = "test"
    expected = '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def special_characters_test():
    s = "!@#$%^&*()_+"
    to_find = "!@#"
    expected = s[0:] + '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def single_character_test():
    s = "X"
    to_find = "X"
    expected = s + '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def whitespace_string_test():
    s = "   \t   "
    to_find = "\t"
    expected = s[3:] + '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def mixed_case_test():
    s = "AbCdEfGhIj"
    to_find = "CdE"
    expected = s[2:] + '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

def edge_case_empty_to_find():
    s = random_string(10)
    to_find = ""
    expected = s + '\n'
    return {
        "cmd": f"./ft_strstr \"{s}\" \"{to_find}\"",
        "output": expected
    }

if __name__ == "__main__":
    tests = {
        1: basic_test,
        2: full_string_test,
        3: no_occurrence_test,
        4: substring_at_start_test,
        5: empty_string_test,
        6: special_characters_test,
        7: single_character_test,
        8: whitespace_string_test,
        9: mixed_case_test,
        10: edge_case_empty_to_find
    }
    gen_tests(tests)
