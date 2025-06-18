#include <stdio.h>
#include <string.h>
#include <ctype.h>

int is_vowel(char c) {
    char lower = tolower(c);
    return (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u');
}

int main(int ac, char **av) {
    if (ac == 2) {
        char *str = av[1];
        for (int i = 0; str[i] != '\0'; i++) {
            if (!is_vowel(str[i])) {
                putchar(str[i]);
            }
        }
    }
    putchar('\n');
    return 0;
}
