#include <stdio.h>
#include <stdlib.h>

char *ft_strcat(char *restrict s1, const char *restrict s2);

int main(int ac, char **av)
{
    if (ac != 3){
        printf("\n");
        return 1;
    }

    printf("%s\n", ft_strcat(av[1], av[2]));
    return 0;
}
