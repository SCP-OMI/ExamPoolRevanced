import random
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_strjoin"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_strjoin.c"

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
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))

def basic_concatenation():
    cmd = '"ForGeeks" "Geeks"'
    return create_test(cmd)

def empty_s2():
    cmd = '"Hello " "World"'
    return create_test(cmd)

def empty_s1():
    cmd = '"Hello" " World!"'
    return create_test(cmd)

def long_strings():
    cmd = '"Tutorials " " point"'
    return create_test(cmd)

def special_characters():
    cmd = '"computer~" " ~program"'
    return create_test(cmd)

def edge_case():
    cmd = '"A" "B"'
    return create_test(cmd)

def null_input():
    cmd = '"Hello" ""'
    return create_test(cmd)

def very_large_strings():
    s1 = random_string(10**6)
    s2 = random_string(10**6)
    cmd = f"\"{s1}\" \"{s2}\""
    return create_test(cmd)

def newline_and_tab():
    cmd = '"Hello\n" "World\t"'
    return create_test(cmd)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: basic_concatenation,
        2: empty_s2,
        3: empty_s1,
        4: long_strings,
        5: special_characters,
        6: edge_case,
        7: null_input,
        8: very_large_strings,
        9: newline_and_tab,
    }
    gen_tests(tests)
