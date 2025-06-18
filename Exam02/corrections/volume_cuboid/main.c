#include <stdio.h>
#include <stdlib.h>

int volume_cuboid(int l, int b, int h);

int main(int ac, char **av)
{
    if (ac != 4){
        printf("\n");
        return 0;
    }

    int l = atoi(av[1]);
    int b = atoi(av[2]);
    int h = atoi(av[3]);

    int volume = volume_cuboid(l, b, h);
    printf("%d\n", volume);
    return 0;
}
