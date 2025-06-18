#include <stdio.h>
#include <stdlib.h>

char *ft_strjoin(const char *s1, const char *s2);

int main(int ac, char **av)
{
    if (ac != 3){
        printf("\n");
        return 1;
    }

    printf("%s\n", ft_strjoin(av[1], av[2]));
    return 0;
}
