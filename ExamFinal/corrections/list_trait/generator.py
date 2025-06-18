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

__author__ = 'Ahlam Raiteb'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "list_trait.c"

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
    
def  basic_test():
    s1 = "2"
    s2 = "1"
    s3 = "6"
    s4 = "9"
    cmd = f"\"{s1}\" \"{s2}\" \"{s3}\" \"{s4}\""
    create_test(cmd)

def  basic_test1():
    s1 = "6"
    s2 = "4"
    s3 = "3"
    s4 = "2"
    cmd = f"\"{s1}\" \"{s2}\" \"{s3}\" \"{s4}\""
    create_test(cmd)

def  basic_test2():
    s1 = "-8"
    s2 = "3"
    s3 = "9"
    s4 = "-6"
    cmd = f"\"{s1}\" \"{s2}\" \"{s3}\" \"{s4}\""
    create_test(cmd)

def  basic_test3():
    s1 = "2"
    s2 = "0"
    s3 = "6"
    s4 = "0"
    cmd = f"\"{s1}\" \"{s2}\" \"{s3}\" \"{s4}\""
    create_test(cmd)

def  basic_test3():
    s1 = "2"
    s2 = "0"
    s3 = "6"
    s4 = "0"
    cmd = f"\"{s1}\" \"{s2}\" \"{s3}\" \"{s4}\""
    create_test(cmd)

def  basic_test4():
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    cmd = f"\"{s1}\" \"{s2}\" \"{s3}\" \"{s4}\""
    create_test(cmd)

def  basic_test5():
    create_test("")

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1 : basic_test,
        2 : basic_test1,
        3 : basic_test2,
        4 : basic_test3,
        5 : basic_test4,
        6 : basic_test5,
    }
    gen_tests(tests)