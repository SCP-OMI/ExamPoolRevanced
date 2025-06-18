import random
import string
from subprocess import call
from deepthought.correction.tests import gen_tests

__author__ = 'Babela Mohamed'
__email__ = "mohamadbabela@gmail.com"

EXP_BIN_NAME = "ft_strdel"
COMPILER = "gcc"
FLAGS = "-Wall -Wextra -Werror"
SRC = "ft_strdel.c main.c"

def compile_expected_program():
    command = "{compiler} {flags} {src} -o {bin_name}" \
        .format(compiler=COMPILER,
                flags=FLAGS,
                src=SRC,
                bin_name=EXP_BIN_NAME)
    call(command, shell=True)
   

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))

def basic_free():
    s = random_string(10)
    return {
        "cmd": f'./ft_strdel "{s}"',
        "output": "Pointer is now NULL",
    }

def empty_string():
    s = ""
    return {
        "cmd": f'./ft_strdel "{s}"',
        "output": "Pointer is now NULL",
    }

def null_pointer():
    s = None
    return {
        "cmd": f'./ft_strdel "{s}"',
        "output": "Pointer is already NULL",
    }

def large_string():
    s = random_string(10**6)
    return {
        "cmd": f'./ft_strdel "{s}"',
        "output": "Pointer is now NULL",
    }

def string_with_spaces():
    s = random_string(10) + " with spaces"
    return {
        "cmd": f'./ft_strdel "{s}"',
        "output": "Pointer is now NULL",
    }

def multiple_free_calls():
    s = random_string(10)
    result = []
    result.append({
        "cmd": f'./ft_strdel "{s}"',
        "output": "Pointer is now NULL",
    })
    result.append({
        "cmd": f'./ft_strdel "{s}"',
        "output": "Pointer is already NULL",
    })
    return result

if __name__ == "__main__":
    tests = {
        1: basic_free,
        2: empty_string,
        3: null_pointer,
        4: large_string,
        5: string_with_spaces,
        6: multiple_free_calls,
    }
    gen_tests(tests)