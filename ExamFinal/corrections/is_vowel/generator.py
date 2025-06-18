import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "ahlam.raiteb@gmail.com"

EXP_BIN_NAME = "is_vowel"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "is_vowel.c"

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

def random_vowel(upper=False):
    vowels = "aeiou"
    if upper:
        return random.choice(vowels.upper())
    return random.choice(vowels)

def random_non_vowel(upper=False):
    non_vowels = "bcdfghjklmnpqrstvwxyz"
    if upper:
        return random.choice(non_vowels.upper())
    return random.choice(non_vowels)

def test_vowel_lowercase():
    v = random_vowel()
    return create_test(v)

def test_vowel_uppercase():
    v = random_vowel(upper=True)
    return create_test(v)

def test_non_vowel_lowercase():
    c = random_non_vowel()
    return create_test(c)

def test_non_vowel_uppercase():
    c = random_non_vowel(upper=True)
    return create_test(c)

def test_non_alphabetic():
    non_alpha = random.choice("1234567890!@#$%^&*() ")
    return create_test(non_alpha)

def test_empty_arg():
    return create_test("")

def test_no_arg():
    return create_test()

def test_multiple_args():
    return {
        "cmd": "./is_vowel a b c",
        "output": "\n"
    }

if __name__ == "__main__":
    tests = {
        1: test_vowel_lowercase,
        2: test_vowel_uppercase,
        3: test_non_vowel_lowercase,
        4: test_non_vowel_uppercase,
        5: test_non_alphabetic,
        6: test_empty_arg,
        7: test_no_arg,
        8: test_multiple_args,
    }
    gen_tests(tests)