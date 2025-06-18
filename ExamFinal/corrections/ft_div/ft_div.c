#include <stdio.h>

void ft_div(int *ptr, int number)
{
    if (!ptr || number == 0)
        return;
    *ptr /= number;
}