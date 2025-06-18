#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

char *ft_strndup(const char *src, size_t n);

static int ft_my_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i = i + 1;
	return (i);
}

int	main(int ac , char **av)
{
	char	*str;
    size_t  n;
	(void) ac;

    n = atoi(av[2]);
	str = ft_strndup(av[1], n);
	printf("%s\n", str);
	free(str);
	return (0);
}
