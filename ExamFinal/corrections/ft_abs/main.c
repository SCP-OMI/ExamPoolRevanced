#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int ft_abs(int n);

int main(int ac, char **av)
{
    if (ac != 2){
        printf("\n");
        return -1;
    }
    int n = atoi(av[1]);
    printf("%d\n",ft_abs(n));
    return 0;
}
