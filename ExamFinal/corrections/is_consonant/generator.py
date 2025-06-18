import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "ahlam.raiteb@gmail.com"

EXP_BIN_NAME = "is_consonant"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "is_consonant.c"

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

def random_consonant(upper=False):
    consonants = "bcdfghjklmnpqrstvwxyz"
    if upper:
        return random.choice(consonants.upper())
    return random.choice(consonants)

def random_vowel(upper=False):
    vowels = "aeiou"
    if upper:
        return random.choice(vowels.upper())
    return random.choice(vowels)

def test_consonant_lowercase():
    c = random_consonant()
    return create_test(c)

def test_consonant_uppercase():
    c = random_consonant(upper=True)
    return create_test(c)

def test_vowel_lowercase():
    v = random_vowel()
    return create_test(v)

def test_vowel_uppercase():
    v = random_vowel(upper=True)
    return create_test(v)

def test_non_alphabetic():
    non_alpha = random.choice("1234567890!@#$%^&*() ")
    return create_test(non_alpha)
def test_empty_arg():
    return create_test("")

def test_no_arg():
    return create_test("wedvfs")

def test_multiple_args():
    cmd = '"d" "e"'
    return create_test(cmd)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: test_consonant_lowercase,
        2: test_consonant_uppercase,
        3: test_vowel_lowercase,
        4: test_vowel_uppercase,
        5: test_non_alphabetic,
        6: test_empty_arg,
        7: test_no_arg,
        8: test_multiple_args,
    }
    gen_tests(tests)
