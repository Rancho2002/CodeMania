#include <stdio.h>

int main()
{
    int row, col,i,j,space;
    row = 5, col = 5,space=3;
    for(i=1;i<=row;i++){
        //D
        for(j=1;j<=col;j++){
            if(i==1 || j==1 || j==col || i==row)
            printf("* ");
            else
            printf("  ");
        }
        
        //space 
        for(j=1;j<=space;j++)
            printf("  ");
        
        //E
        for(j=1;j<=col;j++){
            if(j==1 || i==1 || i==row || i==row/2+1)
            printf("* ");
            else
            printf("  ");
        }

        //space 
        for(j=1;j<=space;j++)
            printf("  ");
            
        //E
        for(j=1;j<=col;j++){
            if(j==1 || i==1 || i==row || i==row/2+1)
            printf("* ");
            else
            printf("  ");
        }

        //space 
        for(j=1;j<=space;j++)
            printf("  ");
        

        for(j=1;j<=col;j++){
            if(i==1 || j==1 || (j==col && i<=3) || i==3)
            printf("* ");
            else
            printf("  ");
        }

        printf("\n");
    }
    return 0;
}