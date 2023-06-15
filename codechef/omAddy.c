#include <stdio.h>

int main(void)
{
    // your code goes here
    int n, c, om = 0, ad = 0, om1 = 0, ad1 = 0;
    scanf("%d", &n);
    ;
    
    for (int j = 0; j< n; j++)
    {
        
        scanf("%d", &c);
        int omm[c], add[c];

        for (int i = 0; i < c; i++)
        {
            scanf("%d", &omm[i]);
        }
        for (int i = 0; i < c; i++)
        {
            scanf("%d", &add[i]);
        }

        for (int i = 0; i < c; i++)
        {

            if (omm[i] != 0)
                om++;
            else
            {
                if (om > om1)
                    om1 = om;
                om = 0;
            }
            if (add[i] != 0)
                ad++;
            else
            {
                if (ad > ad1)
                    ad1 = ad;
                ad = 0;
            }
            // printf("%d %d\n", om, ad);
        }
        // printf("%d %d\n", om1, ad1);
        if (om1 > ad1)
            printf("Om\n");
        else if (ad1 > om1)
            printf("Addy\n");
        else
            printf("Draw\n");

        om1=0,ad1=0;
    }
    return 0;
}
