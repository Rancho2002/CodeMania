#include <stdio.h>
#include <math.h>
int main(void) {
	// your code goes here
    int total,a,b;
    scanf("%d",&total);
    for(int i=0;i<total;i++){
        scanf("%d%d",&a,&b);
        printf("%d\n",abs(a-b));
    }
	return 0;
}

// https://www.codechef.com/submit/POLTHIEF