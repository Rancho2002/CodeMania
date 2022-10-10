// https://www.codechef.com/submit/BESTOFTWO

#include <stdio.h>

int main(void) {
	// your code goes here
	int total, a, b;
	scanf("%d",&total);
	for(int i=0;i<total;i++){
	    scanf("%d%d",&a,&b);
	    printf("%d\n",(a>=b)?a:b); 
	}
	return 0;
}

