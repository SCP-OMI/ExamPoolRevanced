** WARNING - PRODUCTION REPOSITORY **

This repository is used in production by the automated exam system.

This repository is pulled automatically to the exam server every 10 minutes.

Only the owner of this repository will integrate changes, if you want to make modifications, fork this repository, and make a merge request assigned to the maintainer.

# Exam assignment repository

This repository is part of the exam system, and contains :
* The assignment subjects (in subjects/)
* The assignment correction scripts and tests (in corrections/)
* The assignment pools for the intranet's exams (in pools/)

# Contributing

## Creating a new assignment

Let's take the example of an assignment called **stupidcat**

### Creating the subject

Make a directory for the subject. It will be under `subjects/` and have the same name as the assignment.

In our example:
```
mkdir subjects/stupidcat
cd subjects/stupidcat
```

Everything that is in this directory will be given to the user when he receives his assignment.

There needs to be at least a `subject.en.txt` file, that contains the subject of the assignment, with a header that specifies the required files and the allowed functions.
There is a template for subjects that's located in `<repo_root>/subject.en.txt.TEMPLATE`. You really should use it, or it will just give the repository maintainer more work
to integrate your modifications.

The subject should look as follows:

```
Assignment name  : stupidcat
Expected files   : stupidcat.c
Allowed functions: stupidcat
--------------------------------------------------------------------------------

Make a program named stupidcat that displays "stupid cat!" followed by a newline.

Examples:

$>./stupidcat | cat -e
stupid cat!$
$>
```

**Warning**: Please make sure that whatever you include in the subject directory isn't too heavy. For example, if you absolutely want to include huge examples to run with the program, you may want to consider including a generator script instead.

### Creating the correction scripts

_If your assignment is not in C / C++, or requires an atypical correction script, please ask the maintainer. It is very doable, but hard to explain in a readme._

Make a directory for the correction. It will be under `corrections/` and have the same name as the assignment.

In our example:

```
mkdir corrections/stupidcat
cd corrections/stupidcat
```

**deepthought** requires a `profile.yml` file to work. There is a commented template in `<repo_root>/profile.yml.TEMPLATE`:

```
cp ../profile.yml.TEMPLATE profile.yml
vim profile.yml
# [...]
```

The easiest way to correct a C / C++ assignment is to put input//expected_output files in the correction directory, like in the following example (the `wdmatch` assignment on the repository):

```
$> ls -l
total 128
-rw-r--r--  1 zaz  staff  153 Apr 16 14:09 profile.yml
-rw-r--r--  1 zaz  staff   32 Apr 16 14:09 test1.cmd
-rw-r--r--  1 zaz  staff    5 Apr 16 14:09 test1.output
-rw-r--r--  1 zaz  staff   31 Apr 16 14:09 test2.cmd
-rw-r--r--  1 zaz  staff    1 Apr 16 14:09 test2.output
-rw-r--r--  1 zaz  staff   61 Apr 16 14:09 test3.cmd
-rw-r--r--  1 zaz  staff   14 Apr 16 14:09 test3.output
-rw-r--r--  1 zaz  staff   38 Apr 16 14:09 test4.cmd
-rw-r--r--  1 zaz  staff    1 Apr 16 14:09 test4.output
-rw-r--r--  1 zaz  staff   62 Apr 16 14:09 test5.cmd
-rw-r--r--  1 zaz  staff    1 Apr 16 14:09 test5.output
-rw-r--r--  1 zaz  staff   16 Apr 16 14:09 test6.cmd
-rw-r--r--  1 zaz  staff    4 Apr 16 14:09 test6.output
-rw-r--r--  1 zaz  staff    3 Apr 16 14:09 test7.cmd
-rw-r--r--  1 zaz  staff    1 Apr 16 14:09 test7.output
$> cat test1.cmd
"faya" "fgvvfdxcacpolhyghbreda"
$> cat test1.output
faya
```

The `testXXX.cmd` files contain command line arguments that will be passed (verbatim) after the executable name on the commandline, when the moment comes to run the user program. If there are no parameters to give, either make an empty file, or omit the file altogether (An empty file is preferred).
The `testXXX.output` files contain the (verbatim) expected outputs of their respective tests.

**Warning**: Please, please, PLEASE, for the love of whatever you hold dear, do NOT just write your expected outputs yourself : Make your input files, and actually run your program to get the correct output !

For clarity, here's the `profile.yml` file for the `wdmatch` assignment:

```yaml
name: wdmatch

unit: c

compile_user: True

white_list:
    - write

user_files:
    - wdmatch.c

common_files:

tests:
    method: typical
    count: 7
```

You will need to test your correction to make sure it is working correctly. For this, you will also need to actually do the assignment, and put all the expected files in the correction directory. Anyway, as the previous warning says, you'll need it to generate the expected output files.

### Testing your assignment

You will need to use **deepthought** to test your assignment. Make sure it is installed, and that you are in the right virtualenv.

Use the `deepthought-test-single-unit` script, passing the correction directory for your assignment twice on the command line (Once because it contains the source files to test, and once because it's the correction directory with the test files and the profile.yml file).

If it is successful and you validate the assignment, that's a good start, at least your correction works.

Take the time to be thorough while testing and checking for possible mistakes in your assignment : The exam system is automated, so if there is any possibility that your correction is wrong, don't submit it, fix it. Otherwise we'd all risk looking like idiots :)

**REPEAT: BE THOROUGH IN YOUR TESTING. DON'T MAKE US LOOK BAD.**

## Submitting your assignment

Push your modifications to a new branch on your fork of the repository, then make a merge request assigned to the maintainer of the main repository.

If your assignment meets all the criteria, works well, and the subject is readable / without typos, it will be integrated.
