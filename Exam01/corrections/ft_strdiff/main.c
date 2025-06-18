#include <stdio.h>
#include <stdlib.h>

int ft_strdiff(const char *s1, const char *s2);

int main(int ac, char **av)
{
    if (ac != 3){
        printf("\n");
        return 1;
    }

    printf("%d\n", ft_strdiff(av[1], av[2]));
    return 0;
}
