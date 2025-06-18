import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_str_is_alpha"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_str_is_alpha.c main.c"

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

def random_string(length=10, only_alpha=True):
    if only_alpha:
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))
    else:
        chars = string.ascii_letters + string.digits + string.punctuation + " "
        return ''.join(random.choice(chars) for _ in range(length))

def test_only_letters():
    s = random_string(10, only_alpha=True)
    return create_test(s)

def test_numbers():
    s = random_string(5, only_alpha=True) + random.choice(string.digits)
    return create_test(s)

def test_special_characters():
    s = random_string(5, only_alpha=True) + random.choice("!@#$%^&*()")
    return create_test(s)

def test_empty_string():
    s = ""
    return create_test(s)

def test_mixed_string():
    s = random_string(5, only_alpha=True) + "123abc"
    return create_test(s)

if __name__ == "__main__":
    tests = {
        1: test_only_letters,
        2: test_numbers,
        3: test_special_characters,
        4: test_empty_string,
        5: test_mixed_string,
    }
    gen_tests(tests)