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
SRC = "length_words.c"

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
        cmd = "Hello world!"
        return create_test(cmd)
def basic_test1():
    cmd = "Hi there how are you?"
    return create_test(cmd)
  
def basic_test2():
    return{
        "cmd":"",
        "output":"\n",
    }
def empty_test():
    return create_test("")

def random_string():
    string = random.choice(string.printable.strip())
    return create_test(string)

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1: empty_test,
        "2-6": basic_test,
        "6-20": random_string,
        21 : basic_test1,
        22 : basic_test2,
    }
    gen_tests(tests)