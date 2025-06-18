#include <stdio.h>
#include <stdlib.h>

int rectangle_perimeter(int length, int breadth);

int main(int ac, char **av)
{
    if (ac != 3 || av[1][0] == '\0' || av[2][0] == '\0')
    {
        printf("\n");
        return 0;
    }

    int length = atof(av[1]);
    int breadth = atof(av[2]);

    int result = rectangle_perimeter(length, breadth);

    printf("%d\n", result);
    return 0;
}