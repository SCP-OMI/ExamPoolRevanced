#include <stdio.h>

int ascii_character(char c);

int main(int ac, char **av)
{
    if (ac == 2 && av[1][0] != '\0' && av[1][1] == '\0') {
        printf("%d\n", ascii_character(av[1][0]));
    } else {
        putchar('\n');
    }
    return 0;
}