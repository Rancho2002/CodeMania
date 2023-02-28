// https://www.codechef.com/submit/BOBBANK
#include <stdio.h>

int main(void) {
	// your code goes here
	int total,a,b,c,d,e,f,g;
	scanf("%d",&total);
	for(int i=0;i<total;i++){
	    scanf("%d%d%d%d",&a,&b,&c,&d);
	    e=b-c;
	    f=a+e*d;
	    printf("%d\n",f);
	}
	return 0;
}

