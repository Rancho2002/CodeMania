#include <stdio.h>


int main(void) {
	// your code goes here
	int total,a,to;
	long int result;
	scanf("%d",&total);
	for(int i=0;i<total;i++){
	    scanf("%d%d",&a,&to);
	    result=a*to;
	    printf("%d\n",result);
	}
	return 0;
}

