#include <unistd.h>

void print_number(int num)
{
    char c;
    if (num >= 10)
        print_number(num / 10);
    c = (num % 10) + '0';
    write(1, &c, 1);
}

int is_valid_binary(char *str)
{
    if (!str || !*str)
        return (0);
    while (*str)
    {
        if (*str != '0' && *str != '1')
            return (0);
        str++;
    }
    return (1);
}

int binary_to_decimal(char *binary)
{
    int result = 0;
    while (*binary)
    {
        result = result * 2 + (*binary - '0');
        binary++;
    }
    return (result);
}

int main(int argc, char **argv)
{
    if (argc != 2 || !is_valid_binary(argv[1]))
    {
        write(1, "\n", 1);
        return (0);
    }
    print_number(binary_to_decimal(argv[1]));
    write(1, "\n", 1);
    return (0);
}
