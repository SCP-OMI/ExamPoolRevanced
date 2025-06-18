void ft_pow(int *ptr, int number)
{
    int base;
    int result = 1;

    if (!ptr)
        return;
    base = *ptr;
    if (number < 0)
    {
        *ptr = 0;
        return;
    }
    while (number > 0)
    {
        result *= base;
        number--;
    }
    *ptr = result;
}
