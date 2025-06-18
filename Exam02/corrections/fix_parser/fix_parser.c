#include <stdio.h>
#include <ctype.h>
#include <string.h>

int is_valid_expression(const char *str) {
    int i = 0;

    while (str[i] == ' ') i++;

    if (str[i] == '\0') return 0;

    if (!isdigit(str[i])) return 0;

    while (str[i] != '\0') {
        if (isdigit(str[i])) {
            i++;
        }
        else if (str[i] == '+' || str[i] == '-' || str[i] == '*' || str[i] == '/') {
            i++;
            while (str[i] == ' ') i++;
            if (!isdigit(str[i])) return 0;
        }
        else if (str[i] == ' ') {
            i++;
        }
        else {
            return 0;
        }
    }

    return 1;
}
