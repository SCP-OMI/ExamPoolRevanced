#include <stdio.h>

void ft_bubblesort(int *arr, int size);

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        printf("\n");
        return 1;
    }

    int size = argc - 1;
    int arr[size];

    for (int i = 0; i < size; i++)
        arr[i] = atoi(argv[i + 1]);

    ft_bubblesort(arr, size);

    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");

    return 0;
}

