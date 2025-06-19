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

