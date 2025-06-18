#include <stddef.h>

char *ft_strcat(char *restrict s1, const char *restrict s2)
{
    char *original_s1 = s1;
    while (*s1 != '\0')
    {
        s1++;
    }
    while (*s2 != '\0')
    {
        *s1 = *s2;
        s1++;
        s2++;
    }
    *s1 = '\0';
    return original_s1;
}
