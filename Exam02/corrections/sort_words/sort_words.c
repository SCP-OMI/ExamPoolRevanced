#include <stdio.h>
#include <string.h>

void sortWords(char* str)
{
    int i = 0;
    int j = 0;
    int k = 0;
    int spaces = 0;

    char ptr1[50][100];
    char ptr2[50][100];
    char cmp[50];

    while (str[i]) {
        if ((str[i] == ' ') || (str[i] == ',') || (str[i] == '.'))
            spaces++;
        i++;
    }

    for (i = 0; j < strlen(str); j++) {
        if ((str[j] == ' ') || (str[j] == 44) || (str[j] == 46)) {
            ptr2[i][k] = '\0';
            i++;
            k = 0;
        }
        else
            ptr2[i][k++] = str[j];
    }

    for (i = 0; i < spaces; i++) {
        for (j = i + 1; j <= spaces; j++) {
            if ((strcmp(ptr2[i], ptr2[j]) > 0)) {
                strcpy(cmp, ptr2[i]);
                strcpy(ptr2[i], ptr2[j]);
                strcpy(ptr2[j], cmp);
            }
        }
    }
    
    for (i = 0; i <= spaces; i++)
        printf("%s ", ptr2[i]);
    printf("\n");
}

int main(int ac, char **av)
{
   if (ac != 2){
        printf("\n");
        return (1);
   }

    sortWords(av[1]);
    return 0;
}
