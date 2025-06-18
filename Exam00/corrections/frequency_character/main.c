# include <stdio.h>
int frequency_character(char c, char *str);

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("\n");
        return 0;
    }
    
    char c = argv[1][0];
    char *str = argv[2];
    
    int count = frequency_character(c, str);
    printf("%d\n", count);
    
    return 0;
}