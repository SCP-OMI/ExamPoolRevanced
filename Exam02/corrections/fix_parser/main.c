#include <stdio.h>

int is_valid_expression(const char *str);

int main(int argc, char **argv) {
    if (argc != 2)
        return 1;

    if (is_valid_expression(argv[1])) {
        printf("Valid\n");
    } else {
        printf("Invalid\n");
    }

    return 0;
}