#include <stdio.h>
#include <stdlib.h>

int largest_number(int a, int b, int c);

int main(int ac, char **av)
{
    if (ac != 4 || av[1][0] == '\0' || av[2][0] == '\0' || av[3][0] == '\0')
    {
        printf("\n");
        return 0;
    }

    int a = atoi(av[1]);
    int b = atoi(av[2]);
    int c = atoi(av[3]);

    int max = largest_number(a, b, c);
    printf("%d\n", max);
    return 0;
}
