#include <stdio.h>

int ft_strdiff(const char *s1, const char *s2) {
    int i = 0;
    
    while (s1[i] && s2[i]) {
        if (s1[i] != s2[i])
            return i;
        i++;
    }
    
    return (s1[i] != s2[i]) ? i : -1;
}