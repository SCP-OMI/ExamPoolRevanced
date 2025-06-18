#include <stdio.h>
#include <stdlib.h>

int volume_cube(int a);

int main(int ac, char **av)
{
    if (ac != 2){
        printf("\n");
        return 1;
    }

    int a = atoi(av[1]);
    int volume = volume_cube(a);
    printf("%d\n", volume);
    return 0;
}
