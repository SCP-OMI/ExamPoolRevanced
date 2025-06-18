#include <stdio.h>

char prev_character(char c);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("\n");
        return 1;
    }

    char input = argv[1][0];
    char result = prev_character(input);

    printf("%c\n", result);

    return 0;
}