#include <unistd.h>

int is_vowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

int main(int argc, char **argv) {
    if (argc != 2) {
        write(1, "\n", 1);
        return 0;
    }

    char c = argv[1][0];
    if (is_vowel(c))
        write(1, "is vowel\n", 9);
    else
        write(1, "is not vowel\n", 13);

    return 0;
}