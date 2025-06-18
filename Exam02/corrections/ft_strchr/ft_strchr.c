#include <stdio.h>


char *ft_strchr(const char *str, char c)
{
    while (*str != '\0')
    {
        if (*str == c)
            return (char *)str;
        str++;
    }
    if (c == '\0')
        return (char *)str;

    return NULL;
}