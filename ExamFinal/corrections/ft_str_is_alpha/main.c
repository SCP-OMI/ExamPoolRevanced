#include <stdio.h>

int ft_str_is_alpha(char *str);

int main(int ac, char **av)
{
    if (ac != 2)
    {
        printf("\n");
        return 1;
    }
    printf("%d\n",ft_str_is_alpha(av[1]));
    return 0;
}
