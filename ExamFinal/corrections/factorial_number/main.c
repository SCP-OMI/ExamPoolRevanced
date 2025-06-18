#include <stdlib.h>
#include <stdio.h>


int     factorial_number(int num);

int main(int ac, char **av)
{
    if (ac != 2){
        printf("\n");
        return (1);
    }
    
    int n = atoi(av[1]);
    printf("%d\n", factorial_number(n));

    return 0;
}
