#include <stdio.h>
#include <ctype.h>

int main(int ac, char **av)
{
    if (ac != 2)
    {
        printf("\n");
        return 0;
    }

    char *str = av[1];
    int i = 0;
    int len = 0;
    int first = 1;

    while (str[i])
    {
        if (!isspace(str[i]))
        {
            len++;
        }
        else if (len > 0)
        {
            if (!first)
                printf(", ");
            printf("%d", len);
            first = 0;
            len = 0;
        }
        i++;
    }

    if (len > 0)
    {
        if (!first)
            printf(", ");
        printf("%d", len);
    }

    printf("\n");
    return 0;
}
