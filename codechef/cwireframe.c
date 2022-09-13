#include <stdio.h>

int main(void) {
	// your code goes here[//!Solved]
	int total,a,b,c,d;
	long int e;
	scanf("%d",&total);
	for(int i=0;i<total;i++){
	    scanf("%d%d%d",&a,&b,&c);
	    d=2*a+2*b;
	    e=d*c;
	    printf("%ld\n",e);
	}
	return 0;
}

