#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

int* remove_duplicates(int *arr) {
    static int result[MAX_SIZE];
    int exists[MAX_SIZE];
    int i, j, k = 0;
    int found;

    for (i = 0; arr[i] != -1; i++) {
        found = 0;
        for (j = 0; j < k; j++) {
            if (result[j] == arr[i]) {
                found = 1;
                break;
            }
        }
        if (!found) {
            result[k++] = arr[i];
        }
    }

    result[k] = -1;
    return result;
}

