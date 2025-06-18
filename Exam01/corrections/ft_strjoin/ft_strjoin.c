#include <stdlib.h>
#include <string.h>

char *ft_strjoin(const char *s1, const char *s2)
{
    if (!s1 || !s2)
        return NULL;
    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);
    char *joined = (char *)malloc(len1 + len2 + 1);
    if (!joined)
        return NULL;

    strcpy(joined, s1);
    strcat(joined, s2);
    return joined;
}
