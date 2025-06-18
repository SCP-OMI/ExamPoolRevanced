#include <stdlib.h>

void remove_duplicates(int *arr, int *n);

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("\n");
        return 1;
    }

    int input[MAX_SIZE];
    int n = 0;
    char *token = strtok(argv[1], ", ");
    while (token != NULL && n < MAX_SIZE - 1) {
        input[n++] = atoi(token);
        token = strtok(NULL, ", ");
    }
    input[n] = -1;

    int *res = remove_duplicates(input);
    for (int i = 0; res[i] != -1; i++) {
        printf("%d ", res[i]);
    }
    printf("\n");

    return 0;
}
