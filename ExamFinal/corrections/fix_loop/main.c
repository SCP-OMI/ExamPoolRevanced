#include <stdio.h>
#include <string.h>

void	*ft_function(void *b, int c, size_t len);


int main(){
    char str[50];
    int arr[10];

    strcpy(str, "Welcome to Tutorialspoint");
    ft_function(str, '#', 7);
    printf("%s\n",str);

    ft_function(arr, 0, sizeof(arr));
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}