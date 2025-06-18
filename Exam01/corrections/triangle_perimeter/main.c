#include <stdio.h>
#include <stdlib.h>


int triangle_perimeter(int a, int b, int c);

int main(int argc, char **argv)
{
    if (argc != 4 || argv[1][0] == '\0' || argv[2][0] == '\0' || argv[3][0] == '\0')
    {
        printf("\n");
        return 0;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int c = atoi(argv[3]);

    int result = triangle_perimeter(a, b, c);

    printf("%d\n", result);
    return 0;
}