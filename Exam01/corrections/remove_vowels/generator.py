import random
import string
from subprocess import call, check_output
from deepthought.correction.tests import gen_tests

__author__ = 'Ahlam Raiteb'
__email__ = "raiteb.ahlam@gmail.com"

EXP_BIN_NAME = "expected.out"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "remove_vowels.c"

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

def random_string(length=10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
   
def random_strings_test():
    cmd = random_string(16)
    return create_test(cmd)
  
def empty_test():
    return("")  

if __name__ == "__main__":
    compile_expected_program()
    tests = {
        1 : basic_test,
        2 : basic_test1,
        3 : empty_test,
        "3-10":random_strings_test,
    }
    gen_tests(tests)