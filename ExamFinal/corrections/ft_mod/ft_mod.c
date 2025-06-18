void ft_mod(int *ptr, int number)
{
    if (!ptr || number == 0)
        return;
    *ptr %= number;
}