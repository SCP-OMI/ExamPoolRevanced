#include <unistd.h>

int is_valid_decimal(char *str)
{
    if (!str || !*str)
        return (0);
    while (*str)
    {
        if (*str < '0' || *str > '9')
            return (0);
        str++;
    }
    return (1);
}

int str_to_int(char *str)
{
    int result = 0;
    while (*str)
    {
        result = result * 10 + (*str - '0');
        str++;
    }
    return (result);
}

void print_binary(int num)
{
    char binary[32];
    int i = 0;
    
    if (num == 0)
    {
        write(1, "0", 1);
        return;
    }
    while (num > 0)
    {
        binary[i++] = (num % 2) + '0';
        num /= 2;
    }
    while (--i >= 0)
        write(1, &binary[i], 1);
}

int main(int argc, char **argv)
{
    if (argc != 2 || !is_valid_decimal(argv[1]))
    {
        write(1, "\n", 1);
        return (0);
    }
    print_binary(str_to_int(argv[1]));
    write(1, "\n", 1);
    return (0);
}
