#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int is_consonant(char c);

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        write(1, "\n", 1);
        return 0;
    }

    char c = argv[1][0];

    if (is_consonant(c))
        write(1, "is consonant\n", 13);
    else
        write(1, "is not consonant\n", 17);

    return 0;
}