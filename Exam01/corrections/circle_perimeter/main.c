#include <stdio.h>
#include <stdlib.h>

float circle_perimeter(float radius);

int main(int argc, char **argv)
{
    if (argc != 2 || argv[1][0] == '\0')
    {
        printf("\n");
        return 0;
    }

    float radius = atof(argv[1]);
    float result = circle_perimeter(radius);

    printf("%f\n", result);
    return 0;
}