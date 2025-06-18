#include <stdlib.h>

char *ft_strndup(const char *src, size_t n)
{
    size_t i;
    char *dup;

    if (!src)
        return NULL;
    dup = malloc(sizeof(char) * (n + 1));
    if (!dup)
        return NULL;
    i = 0;
    while (i < n && src[i])
    {
        dup[i] = src[i];
        i++;
    }
    dup[i] = '\0';
    return dup;
}
