#include <stdio.h>

int main(int ac, char **av)
{
    if (ac == 2 && av[1][0] != '\0' && av[1][1] == '\0') {
        printf("%d\n", av[1][0]);
    } else {
        putchar('\n');
    }
    
    return 0;
}
