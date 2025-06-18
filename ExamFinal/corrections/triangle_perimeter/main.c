#include <stdio.h>
#include <stdlib.h>


float triangle_perimeter(float a, float b, float c);

int main(int argc, char **argv)
{
    if (argc != 4 || argv[1][0] == '\0' || argv[2][0] == '\0' || argv[3][0] == '\0')
    {
        printf("\n");
        return 0;
    }

    float a = atof(argv[1]);
    float b = atof(argv[2]);
    float c = atof(argv[3]);

    float result = triangle_perimeter(a, b, c);

    printf("%.2f\n", result);
    return 0;
}