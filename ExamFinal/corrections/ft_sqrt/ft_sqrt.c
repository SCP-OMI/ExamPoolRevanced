#include <stdio.h>

void ft_sqrt(int *ptr, int number) {
    if (number < 0) {
        *ptr = -1;
        return;
    }
    int sqrt = 0;
    while (sqrt * sqrt <= number) {
        if (sqrt * sqrt == number) {
            *ptr = sqrt;
            return;
        }
        sqrt++;
    }
    *ptr = -1;
}
