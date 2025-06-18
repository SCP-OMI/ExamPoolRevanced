#include <stdio.h>

char *ft_strstr(char *str, char *to_find);

int main(int ac, char **av)
{
    if(ac != 3){
        printf("\n");
        return 0;
    }
    char *result = ft_strstr(av[1], av[2]);
    if (result)
        printf("%s\n", result);
    else
        printf("\n");

    return 0;
}
