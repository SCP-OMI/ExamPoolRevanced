#include <stdio.h>
#include <string.h>

int main(int ac, char **av)
{
    if (ac != 2)
    {
        printf("\n");
        return 0;
    }

    if (strcmp(av[1], "int") == 0)
        printf("%zu bytes\n", sizeof(int));
    else if (strcmp(av[1], "char") == 0)
        printf("%zu bytes\n", sizeof(char));
    else if (strcmp(av[1], "float") == 0)
        printf("%zu bytes\n", sizeof(float));
    else if (strcmp(av[1], "double") == 0)
        printf("%zu bytes\n", sizeof(double));
    else
        printf("\n");

    return 0;
}
