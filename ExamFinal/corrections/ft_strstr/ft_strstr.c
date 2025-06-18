char *ft_strstr(char *str, char *to_find)
{
    if (!*to_find)
        return str;

    while (*str)
    {
        char *s = str;
        char *f = to_find;

        while (*s && *f && *s == *f)
        {
            s++;
            f++;
        }

        if (*f == '\0')
            return str;

        str++;
    }

    return 0;
}
