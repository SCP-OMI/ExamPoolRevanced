#include <stdio.h>
#include <stdlib.h>

float rectangle_perimeter(float length, float breadth);

int main(int ac, char **av)
{
    if (ac != 3 || av[1][0] == '\0' || av[2][0] == '\0')
    {
        printf("\n");
        return 0;
    }

    float length = atof(av[1]);
    float breadth = atof(av[2]);

    float result = rectangle_perimeter(length, breadth);

    printf("%.2f\n", result);
    return 0;
}