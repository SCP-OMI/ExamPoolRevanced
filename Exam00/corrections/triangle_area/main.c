#include <stdio.h>
#include <stdlib.h>

int     triangle_area(int base, int height);

int main(int ac, char **av) {
    if (ac != 3){
        printf("\n");
        return (1);
    }

    
    int n = atof(av[1]);
    int n1 = atof(av[2]);

    printf("%d\n",triangle_area(n, n1));
    return (0);
}