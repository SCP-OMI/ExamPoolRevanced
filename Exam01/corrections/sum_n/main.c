#include <stdio.h>

int sum_n(int n);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("\n");
        return 1;
    }

    int n = atoi(argv[1]);
    printf("%d\n", sum_n(n));

    return 0;
}
