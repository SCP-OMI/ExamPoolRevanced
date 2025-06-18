#include <stdio.h>
#include <stdlib.h>

char *ft_strchr(const char *str, char c);

int main(int ac, char **av)
{
    if (ac != 3 || av[2][0] != '\0' || av[2][1] == '\0'){
        printf('\n');
        return 1;
    }

    printf("%s\n", ft_strchr(av[1], av[2]));
    return 0;
}
