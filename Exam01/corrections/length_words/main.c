#include <stdio.h>


int main(int ac, char **av)
{
    if (ac != 2)
    {
        printf("\n");
        return 0;
    }

    length_words(av[1]);
    return 0;
}