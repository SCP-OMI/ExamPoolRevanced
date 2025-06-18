#include <unistd.h>
#include <stdlib.h>

int is_even(int number) {
    return (number % 2 == 0);
}

int sum_up_to(int n) {
    int total = 0;
    int i = 1;
    while(i <= n) {
        total += i;
        i++;
    }
    return total;
}

void int_to_str(int num, char *buffer, int *length) {
    int i = 0;
    int is_negative = 0;

    if (num < 0) {
        is_negative = 1;
        num = -num;
    }

    if (num == 0) {
        buffer[i++] = '0';
    } else {
        while (num > 0) {
            buffer[i++] = (num % 10) + '0';
            num /= 10;
        }
    }

    if (is_negative) {
        buffer[i++] = '-';
    }

    int start = 0, end = i - 1;
    while (start < end) {
        char temp = buffer[start];
        buffer[start] = buffer[end];
        buffer[end] = temp;
        start++;
        end--;
    }

    *length = i;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        write(STDERR_FILENO, "Error !\n", 26);
        exit(1);
    }

    int num = atoi(argv[1]);
    char buffer[20];
    int len;

    int_to_str(num, buffer, &len);
    write(STDOUT_FILENO, buffer, len);
    if (is_even(num)) {
        write(STDOUT_FILENO, " is even\n", 9);
    } else {
        write(STDOUT_FILENO, " is odd\n", 8);
    }

    int sum = sum_up_to(num);
    int_to_str(sum, buffer, &len);
    
    write(STDOUT_FILENO, "Sum from 1 to ", 14);
    int_to_str(num, buffer, &len);
    write(STDOUT_FILENO, buffer, len);
    write(STDOUT_FILENO, " is: ", 5);
    int_to_str(sum, buffer, &len);
    write(STDOUT_FILENO, buffer, len);
    write(STDOUT_FILENO, "\n", 1);

    return 0;
}