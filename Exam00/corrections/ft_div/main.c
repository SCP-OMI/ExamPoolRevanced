#include <stdio.h>
#include <stdlib.h>

int ft_div(int ptr, int number);


int main(int argc, char **argv)
{
    if (argc != 3){
        printf("\n");
        return 1;
    }

    int value = atoi(argv[1]);
    int divisor = atoi(argv[2]);

    int val = ft_div(value, divisor);
    printf("%d\n", val);

    return 0;
}
