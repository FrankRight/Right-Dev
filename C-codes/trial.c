#include <stdio.h>
#include <ctype.h>

int main()
{
    char marks[2];
    int isTrue = 1;

    while(isTrue == 1) {
        printf("Enter your marks: ");
        scanf("%s", marks);

        int count=0;

        for(int i=0; marks[i] != '\0'; i++){
            if(marks[i]!=' ')
            {
                count++;
            }
            
        }

        if (count < 3 && count > 0) {
            if((isdigit(marks[0]) == 2048 && isdigit(marks[1]) == 2048) || (isdigit(marks[0]) == 2048 && count == 1)) {
                printf("%s \n", marks);
                isTrue = 0;
            }
            else {
                printf("\nError!! Invalid marks!! Try Again\n");
            }
        }

        else {
            printf("\nError!! More then Required marks range!! Try Again!\n");
        }
    }

}