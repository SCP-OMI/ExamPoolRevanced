void	*ft_function(void *b, int c, size_t len)
{
	size_t			i;
	unsigned char	*dr;

	dr = (unsigned char *)b;
	i = 0;
	while (len > 0)
	{
		while (i < len)
		{
			dr[i] = c;
			i++;
		}
		len--;
	}
	return (b);
}
