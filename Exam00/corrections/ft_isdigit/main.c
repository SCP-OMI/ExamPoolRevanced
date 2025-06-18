#include <stdio.h>
#include <stdlib.h>

int ft_isdigit(int c);

int main(int ac, char **av)
{
    if (ac != 2){
        printf("\n");
        return 1;
    }

    int n = atoi(av[1]);

    printf("%d\n", ft_isdigit(n));

    return 0;
}