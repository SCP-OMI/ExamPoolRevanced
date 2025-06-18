#include <stdio.h>

void ft_sqrt(int *ptr, int number);

int main(int argc, char **argv)
{
    int result;

    if (argc != 2){
        printf("\n");
        return 1;
    }

    int num = atoi(argv[1]);

    ft_sqrt(&result, num);
    printf("%d\n", result);

    return 0;
}
