// https://www.codechef.com/submit/MOVIE2X
#include <stdio.h>

int main(void) {
	// your code goes here
	int a,b,c,d,rem;
	scanf("%d%d",&a,&b);
	c=b/2;
	rem=a-b;
	d=rem+c;
	printf("%d",d);
	return 0;
}

