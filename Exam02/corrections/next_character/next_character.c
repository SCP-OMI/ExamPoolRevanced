#include <stdio.h>

int main(int ac, char **av)
{
    if (ac != 2 || av[1][0] == '\0' || av[1][1] != '\0')
    {
        printf("\n");
        return 0;
    }

    char c = av[1][0];

    if (c == 'z')
        c = 'a';
    else if (c == 'Z')
        c = 'A';
    else
        c += 1;

    printf("%c\n", c);
    return 0;
}
