#include <stdio.h>
#include <stdlib.h>

int     rectangle_area(int length, int breadth);

int main(int ac, char **av) {
    if (ac != 3){
        printf("\n");
        return (1);
    }
    
    int n = atoi(av[1]);
    int n1 = atoi(av[2]);

    printf("%d\n", rectangle_area(n, n1));
    return (0);
}