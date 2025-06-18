#include <unistd.h>

int is_lower_consonant(char c)
{
    return (c >= 'b' && c <= 'z' && c != 'e' && c != 'i' && c != 'o' && c != 'u');
}

int is_upper_consonant(char c)
{
    return (c >= 'B' && c <= 'Z' && c != 'E' && c != 'I' && c != 'O' && c != 'U');
}

int is_consonant(char c)
{
    return (is_lower_consonant(c) || is_upper_consonant(c));
}

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