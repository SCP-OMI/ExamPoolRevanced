#include <stdio.h>
#include <stdlib.h>

int ft_pow(int ptr, int number);


int main(int argc, char **argv)
{
    if (argc != 3){
        printf("\n")
        return 1;
    }

    int value = atoi(argv[1]);
    int power = atoi(argv[2]);

    int val = ft_pow(value, power);
    printf("%d\n", val);

    return 0;
}
