import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_strdiff.c main.c"

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
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def basic_test():
    s1 = "hello"
    s2 = "hella"
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def identical_strings_test():
    s1 = "test"
    s2 = "test"
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def prefix_test():
    s1 = "abc"
    s2 = "abcd"
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def longer_first_test():
    s1 = "abcd"
    s2 = "abc"
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def empty_vs_nonempty_test():
    s1 = ""
    s2 = random_string(5)
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def random_strings_test():
    s1 = random_string(10)
    s2 = s1[:5] + random.choice(string.ascii_letters) + s1[6:]
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_test,
        2: identical_strings_test,
        3: prefix_test,
        4: longer_first_test,
        5: empty_vs_nonempty_test,
        6: random_strings_test,
    }
    gen_tests(tests)